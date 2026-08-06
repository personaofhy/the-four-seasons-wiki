#!/usr/bin/env python3
"""
ComfyUI Character Image Generator for The Four Seasons Wiki
-----------------------------------------------------------
Generates consistent character pixel art using IP-Adapter (for character face/style)
and ControlNet (for pose/expression), then quantizes output into season 16-color palettes.

Usage example:
    python3 scripts/generate_character_image.py --character momoka --prompt "red cheeks, embarrassed, profile view" --output-name momoka_emotion_blush
"""

import os
import sys
import json
import time
import argparse
import urllib.request
import urllib.error
from PIL import Image

COMFYUI_URL = os.environ.get("COMFYUI_URL", "http://192.168.40.23:8188")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_AI_DIR = os.path.join(BASE_DIR, "content", "assets", "base-ai")
INTERMEDIATE_DIR = os.path.join(BASE_DIR, "content", "assets", "intermediates")
STRICT_16_DIR = os.path.join(BASE_DIR, "content", "assets", "strict-16colors")

# Season 16-Color Palettes
PALETTES = {
    "spring": [
        "#E5A1C8", "#4F5862", "#F0D5C3", "#1A2B44",
        "#8C2A3F", "#DBDFE3", "#334B76", "#667C4D",
        "#121922", "#808D96", "#2A636A", "#9D634C",
        "#3D5C40", "#6E7D88", "#EFE1C9", "#493322"
    ],
    "summer": [
        "#F4D03F", "#2E4053", "#F5B7B1", "#1B4F72",
        "#C0392B", "#FBFCFC", "#5DADE2", "#27AE60",
        "#17202A", "#85929E", "#117864", "#D35400",
        "#1E8449", "#566573", "#F9E79F", "#6E2C00"
    ]
}

CHARACTER_CONFIGS = {
    "momoka": {
        "season": "spring",
        "base_ref": "momoka_expr1_base.jpg",
        "default_prompt": "pixel art, 16-bit retro game sprite, masterpiece, best quality, detailed pixel sprite, 1girl, Momoka Tanabe, ash-brown short bob hair, light green collared shirt, dark jacket, PC-98 pixel game style"
    },
    "himawari": {
        "season": "summer",
        "base_ref": "himawari_expr1_base.jpg",
        "default_prompt": "pixel art, 16-bit retro game sprite, masterpiece, best quality, detailed pixel sprite, 1girl, Kaneshiro Himawari, short black hair, yellow shirt, PC-98 pixel game style"
    }
}

def upload_image_to_comfyui(filepath):
    """Uploads a local image file to ComfyUI input folder."""
    filename = os.path.basename(filepath)
    with open(filepath, "rb") as f:
        img_bytes = f.read()

    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="image"; filename="{filename}"\r\n'
        f"Content-Type: image/jpeg\r\n\r\n"
    ).encode("utf-8") + img_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(
        f"{COMFYUI_URL}/upload/image",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
    )
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode("utf-8"))
    print(f"Uploaded {filename} to ComfyUI: {result}")
    return filename

def build_workflow(character_ref, pose_ref, prompt_text, seed, ip_weight=0.85, cn_weight=0.7, filename_prefix="momoka_gen"):
    """Constructs ComfyUI workflow JSON with IP-Adapter and ControlNet."""
    return {
        "1": {"inputs": {"ckpt_name": "Counterfeit-V3.0_fix_fp16.safetensors"}, "class_type": "CheckpointLoaderSimple"},
        "2": {
            "inputs": {
                "lora_name": "pixel-000020.safetensors",
                "strength_model": 1.0,
                "strength_clip": 1.0,
                "model": ["1", 0],
                "clip": ["1", 1]
            },
            "class_type": "LoraLoader"
        },
        "3": {"inputs": {"ipadapter_file": "ip-adapter_sd15.safetensors"}, "class_type": "IPAdapterModelLoader"},
        "4": {"inputs": {"clip_name": "clip_vision_h.safetensors"}, "class_type": "CLIPVisionLoader"},
        "5": {"inputs": {"image": character_ref}, "class_type": "LoadImage"},
        "6": {
            "inputs": {
                "model": ["2", 0],
                "ipadapter": ["3", 0],
                "image": ["5", 0],
                "clip_vision": ["4", 0],
                "weight": ip_weight,
                "weight_type": "linear",
                "combine_embeds": "concat",
                "start_at": 0.0,
                "end_at": 1.0,
                "embeds_scaling": "V only"
            },
            "class_type": "IPAdapterAdvanced"
        },
        "7": {"inputs": {"control_net_name": "control_v11p_sd15_canny_fp16.safetensors"}, "class_type": "ControlNetLoader"},
        "8": {"inputs": {"image": pose_ref}, "class_type": "LoadImage"},
        "9": {
            "inputs": {
                "positive": ["10", 0],
                "negative": ["11", 0],
                "control_net": ["7", 0],
                "image": ["8", 0],
                "strength": cn_weight,
                "start_percent": 0.0,
                "end_percent": 0.85
            },
            "class_type": "ControlNetApplyAdvanced"
        },
        "10": {"inputs": {"text": prompt_text, "clip": ["2", 1]}, "class_type": "CLIPTextEncode"},
        "11": {
            "inputs": {
                "text": "long hair, black hair, ponytail, western face, realistic photo, 3d render, smooth digital painting, vector, glossy, smooth skin, blurry, bad anatomy",
                "clip": ["2", 1]
            },
            "class_type": "CLIPTextEncode"
        },
        "12": {"inputs": {"width": 512, "height": 768, "batch_size": 1}, "class_type": "EmptyLatentImage"},
        "13": {
            "inputs": {
                "seed": seed,
                "steps": 25,
                "cfg": 7.0,
                "sampler_name": "euler_ancestral",
                "scheduler": "karras",
                "denoise": 1.0,
                "model": ["6", 0],
                "positive": ["9", 0],
                "negative": ["9", 1],
                "latent_image": ["12", 0]
            },
            "class_type": "KSampler"
        },
        "14": {"inputs": {"samples": ["13", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
        "15": {"inputs": {"filename_prefix": filename_prefix, "images": ["14", 0]}, "class_type": "SaveImage"}
    }

def quantize_to_palette(img, hex_palette):
    """Quantizes PIL Image into exact 16-color palette without dithering."""
    palette_rgb = []
    for h in hex_palette:
        h = h.lstrip("#")
        palette_rgb.append(tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

    palette_img = Image.new("P", (1, 1))
    flat_palette = []
    for r, g, b in palette_rgb:
        flat_palette.extend([r, g, b])
    flat_palette.extend([0, 0, 0] * (256 - len(palette_rgb)))
    palette_img.putpalette(flat_palette)

    small = img.resize((256, 384), Image.Resampling.BILINEAR)
    quant = small.quantize(palette=palette_img, dither=Image.Dither.NONE)
    return quant.convert("RGB").resize(img.size, Image.Resampling.NEAREST)

def main():
    parser = argparse.ArgumentParser(description="Generate character images via ComfyUI pipeline")
    parser.add_argument("--character", choices=["momoka", "himawari"], default="momoka", help="Target character")
    parser.add_argument("--prompt", type=str, default="", help="Additional prompt tags")
    parser.add_argument("--pose-ref", type=str, default="himawari_emotion_blush_base.jpg", help="Pose reference image filename in base-ai")
    parser.add_argument("--seed", type=int, default=555123, help="Random seed")
    parser.add_argument("--output-name", type=str, default="momoka_emotion_blush", help="Output filename base")
    args = parser.parse_args()

    os.makedirs(INTERMEDIATE_DIR, exist_ok=True)
    os.makedirs(STRICT_16_DIR, exist_ok=True)

    char_cfg = CHARACTER_CONFIGS[args.character]
    char_ref_path = os.path.join(BASE_AI_DIR, char_cfg["base_ref"])
    pose_ref_path = os.path.join(BASE_AI_DIR, args.pose_ref)

    # Upload reference images
    char_ref_name = upload_image_to_comfyui(char_ref_path)
    pose_ref_name = upload_image_to_comfyui(pose_ref_path)

    full_prompt = f"{char_cfg['default_prompt']}, {args.prompt}"
    workflow = build_workflow(
        character_ref=char_ref_name,
        pose_ref=pose_ref_name,
        prompt_text=full_prompt,
        seed=args.seed,
        filename_prefix=args.output_name
    )

    data = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(f"{COMFYUI_URL}/prompt", data=data, headers={"Content-Type": "application/json"})
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode("utf-8"))
    prompt_id = result["prompt_id"]
    print(f"Workflow submitted. Prompt ID: {prompt_id}")

    # Wait for completion
    while True:
        time.sleep(2)
        h_req = urllib.request.urlopen(f"{COMFYUI_URL}/history/{prompt_id}")
        h_data = json.loads(h_req.read().decode("utf-8"))
        if prompt_id in h_data:
            outputs = h_data[prompt_id]["outputs"]
            for node_id, output in outputs.items():
                if "images" in output:
                    img_info = output["images"][0]
                    filename = img_info["filename"]
                    subfolder = img_info["subfolder"]
                    img_type = img_info["type"]
                    img_url = f"{COMFYUI_URL}/view?filename={filename}&subfolder={subfolder}&type={img_type}"
                    img_bytes = urllib.request.urlopen(img_url).read()

                    # Save Raw to intermediates
                    raw_inter_path = os.path.join(INTERMEDIATE_DIR, f"{args.output_name}_raw.png")
                    with open(raw_inter_path, "wb") as f:
                        f.write(img_bytes)
                    print(f"Saved raw intermediate: {raw_inter_path}")

                    # Quantize and save 16colors to intermediates and strict-16colors
                    raw_img = Image.open(raw_inter_path)
                    quant_img = quantize_to_palette(raw_img, PALETTES[char_cfg["season"]])

                    strict_path = os.path.join(STRICT_16_DIR, f"{args.output_name}_strict_16colors.png")
                    quant_img.save(strict_path)

                    raw_strict_path = os.path.join(STRICT_16_DIR, f"{args.output_name}_comfyui_raw.png")
                    raw_img.save(raw_strict_path)

                    print(f"Saved strict 16colors: {strict_path}")
                    print(f"Saved comfyui raw: {raw_strict_path}")
            break

if __name__ == "__main__":
    main()

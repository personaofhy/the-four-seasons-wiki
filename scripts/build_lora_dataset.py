#!/usr/bin/env python3
"""Generate a LoRA training set for one character from their settled face.

Identity comes from IP-Adapter at high weight, which is reliable as long as we
only ask for neutral faces - the expression bleed that makes IP-Adapter useless
for expression sheets is harmless here, because neutral is what we want. The
variation is in angle, framing and light, which is what a LoRA needs to learn a
face rather than a photograph.

Images land in datasets/<character>/ and are gitignored; this script is the
reproducible part, not its output.

  python3 scripts/build_lora_dataset.py momoka --limit 4      # sample first
  python3 scripts/build_lora_dataset.py momoka                # the whole matrix
"""
import argparse, itertools, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHARACTERS = {
    "momoka": {
        "ref": "wiki/assets/characters/momoka/ref/momoka_face_canon.png",
        "identity": "23yo japanese woman, short light brown hair",
    },
}

ANGLES = [
    "facing the camera straight on",
    "three-quarter view turned left",
    "three-quarter view turned right",
    "chin lowered, eyes up to camera",
    "chin raised, eyes down to camera",
    "near profile from the side",
]
SHOTS = [
    "close-up of the face",
    "head and shoulders portrait",
    "upper body, waist up",
]
LIGHTS = [
    "soft even studio light",
    "window light from one side",
    "flat overcast daylight",
    "warm indoor lamp light",
]
# Clothing has to vary or the LoRA folds the garment into the identity and the
# character can never be dressed in anything else. Lengths 7 and 5 are coprime
# with the 24-cell angle x light grid, so these decorrelate instead of lining up.
CLOTHES = [
    "a plain white t-shirt",
    "a light sage green blouse buttoned to the collar",
    "a charcoal knit sweater",
    "a navy blazer over a white shirt",
    "a black turtleneck",
    "a beige cardigan",
    "a grey hoodie",
]
BACKGROUNDS = [
    "plain grey studio backdrop",
    "plain white backdrop",
    "blurred indoor room",
    "blurred classroom",
    "blurred outdoor greenery",
]

NEGATIVE = ("anime, illustration, cartoon, 3d render, cgi, plastic skin, smiling, "
            "laughing, open mouth, sweating, blush, worst quality, low quality, "
            "text, watermark, deformed, extra fingers, multiple people")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("character", choices=sorted(CHARACTERS))
    ap.add_argument("--limit", type=int, help="generate only the first N")
    ap.add_argument("--start", type=int, default=0)
    args = ap.parse_args()

    spec = CHARACTERS[args.character]
    outdir = os.path.join("datasets", args.character)
    os.makedirs(os.path.join(ROOT, outdir), exist_ok=True)

    # Cycle every other axis against the angle x light grid on coprime periods so
    # no two axes stay locked together across the set.
    combos = [(a, SHOTS[i % len(SHOTS)], l, CLOTHES[i % len(CLOTHES)],
               BACKGROUNDS[i % len(BACKGROUNDS)])
              for i, (a, l) in enumerate(itertools.product(ANGLES, LIGHTS))]
    combos = combos[args.start:]
    if args.limit:
        # Spread the sample across the matrix instead of taking a clumped prefix.
        step = max(1, len(combos) // args.limit)
        combos = combos[::step][:args.limit]

    print(f"{len(combos)} 枚を生成 -> {outdir}/")
    for n, (angle, shot, light, cloth, bg) in enumerate(combos):
        # Framing and angle go first. Late tokens lose to early ones, and with
        # them at the tail the reference's own front-on framing won every time.
        prompt = (f"{shot}, {angle}, photo of a {spec['identity']}, "
                  f"neutral expression, wearing {cloth}, {light}, {bg}, photorealistic")
        name = f"{args.character}_{args.start + n:02d}.png"
        print(f"\n[{n+1}/{len(combos)}] {angle} / {shot} / {cloth} / {light} / {bg}")
        cmd = [
            sys.executable, os.path.join(ROOT, "scripts", "comfy_run.py"),
            "char_ipadapter_sdxl",
            "--set", "CKPT=RealVisXL_V5.0_fp16.safetensors",
            "--set", f"CHARACTER_REF={os.path.basename(spec['ref'])}",
            "--set", "IP_WEIGHT=0.8", "--set", "IP_END=0.85",
            # "linear" also copies the reference's composition, so every image came out
            # dead-on front. "style transfer" keeps the appearance and frees the pose.
            "--set", "WEIGHT_TYPE=style transfer",
            "--set", "LORA_NAME=Hyper-SDXL-8steps-CFG-lora.safetensors",
            "--set", "LORA_STRENGTH=0.0",
            "--set", "WIDTH=832", "--set", "HEIGHT=1024",
            "--set", "STEPS=25", "--set", "CFG=5.0",
            "--set", f"PROMPT={prompt}",
            "--set", f"NEGATIVE_PROMPT={NEGATIVE}",
            "--set", f"FILENAME_PREFIX=ds_{args.character}",
            "--out", f"{outdir}/{name}",
        ]
        if subprocess.run(cmd, cwd=ROOT).returncode:
            sys.exit(f"stopped at {name}")


if __name__ == "__main__":
    main()

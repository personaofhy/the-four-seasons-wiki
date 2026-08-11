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
        # Square-padded pair for the wide batch. Face alone pulls the framing to a
        # bust shot and leaves the build to the model's own guess; the body sheet
        # is what fixes the proportions the author actually specified.
        "face_sq": "wiki/assets/characters/momoka/ref/momoka_ref_face_sq.png",
        "body_sq": "wiki/assets/characters/momoka/ref/momoka_ref_body_sq.png",
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

# The base grid came out 15/24 frontal, which is too front-heavy to teach a head
# in the round. These two supplements correct that and add the missing distances.
ANGLES_TURNED = [
    "full profile from her left",
    "full profile from her right",
    "deep three-quarter, face turned well to her left",
    "deep three-quarter, face turned well to her right",
    "looking back over her shoulder",
    "head turned away, three-quarter from behind",
    "chin dropped low, looking steeply up at the camera",
    "chin lifted high, looking steeply down at the camera",
]
SHOTS_WIDE = [
    "full body standing, head to feet",
    "three-quarter length, knees up",
    "full body at a distance, small in frame",
]

NEGATIVE = ("anime, illustration, cartoon, 3d render, cgi, plastic skin, smiling, "
            "laughing, open mouth, sweating, blush, worst quality, low quality, "
            "text, watermark, deformed, extra fingers, multiple people")

# Full-body needs a taller frame or the figure is cropped and the face is mush.
BATCHES = {
    "base":   {"size": ("832", "1024"), "dual": False},
    "turned": {"size": ("832", "1024"), "dual": False},
    "wide":   {"size": ("768", "1280"), "dual": True},
}

# The body sheet is a nude reference, so the wide batch has to say so in the
# negative or the clothing prompt loses to it.
NEGATIVE_CLOTHED = "nude, naked, topless, underwear, bare skin, cropped head, "


def build(batch, spec):
    """Return (angle, shot, light, cloth, bg) tuples for the named batch."""
    if batch == "base":
        grid = list(itertools.product(ANGLES, LIGHTS))
        shots = SHOTS
    elif batch == "turned":
        grid = [(a, LIGHTS[i % len(LIGHTS)]) for i, a in enumerate(ANGLES_TURNED)]
        shots = SHOTS
    else:
        grid = [(a, l) for l in LIGHTS[:2] for a in ANGLES[:3]]
        shots = SHOTS_WIDE
    return [(a, shots[i % len(shots)], l, CLOTHES[i % len(CLOTHES)],
             BACKGROUNDS[i % len(BACKGROUNDS)]) for i, (a, l) in enumerate(grid)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("character", choices=sorted(CHARACTERS))
    ap.add_argument("--batch", choices=sorted(BATCHES), default="base")
    ap.add_argument("--limit", type=int, help="generate only the first N")
    ap.add_argument("--start", type=int, default=0)
    args = ap.parse_args()

    spec = CHARACTERS[args.character]
    outdir = os.path.join("datasets", args.character)
    os.makedirs(os.path.join(ROOT, outdir), exist_ok=True)

    width, height = BATCHES[args.batch]["size"]
    dual = BATCHES[args.batch]["dual"]
    combos = build(args.batch, spec)
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
        negative = NEGATIVE
        if dual:
            negative = NEGATIVE_CLOTHED + NEGATIVE
            refs = ["--set", f"FACE_REF={os.path.basename(spec['face_sq'])}",
                    "--set", f"BODY_REF={os.path.basename(spec['body_sq'])}",
                    "--set", "FACE_WEIGHT=0.8", "--set", "BODY_WEIGHT=0.45",
                    "--set", "IP_END=0.85"]
        else:
            refs = ["--set", f"CHARACTER_REF={os.path.basename(spec['ref'])}",
                    "--set", "IP_WEIGHT=0.8", "--set", "IP_END=0.85",
                    # "linear" also copies the reference's composition, so every image
                    # came out dead-on front. "style transfer" frees the pose.
                    "--set", "WEIGHT_TYPE=style transfer",
                    "--set", "LORA_NAME=Hyper-SDXL-8steps-CFG-lora.safetensors",
                    "--set", "LORA_STRENGTH=0.0"]
        cmd = [
            sys.executable, os.path.join(ROOT, "scripts", "comfy_run.py"),
            "char_ipadapter_dual_sdxl" if dual else "char_ipadapter_sdxl",
            "--set", "CKPT=RealVisXL_V5.0_fp16.safetensors",
            *refs,
            "--set", f"WIDTH={width}", "--set", f"HEIGHT={height}",
            "--set", "STEPS=25", "--set", "CFG=5.0",
            "--set", f"PROMPT={prompt}",
            "--set", f"NEGATIVE_PROMPT={negative}",
            "--set", f"FILENAME_PREFIX=ds_{args.character}",
            "--out", f"{outdir}/{name}",
        ]
        if subprocess.run(cmd, cwd=ROOT).returncode:
            sys.exit(f"stopped at {name}")


if __name__ == "__main__":
    main()

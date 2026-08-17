FROM python:3.11-slim

RUN apt-get update -qq && apt-get install -y -qq --no-install-recommends \
      git ffmpeg libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/Aratako/Irodori-TTS.git /work
WORKDIR /work

# torch>=2.10 has no macOS x86_64 wheel, which is why this runs inside a
# linux/amd64 container rather than directly on an Intel Mac.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir torch torchaudio torchcodec --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir \
         huggingface-hub numba llvmlite peft pyyaml safetensors soundfile \
         "sentencepiece>=0.1.99,<0.2" "transformers>=5.12.1,<6" tqdm \
    && pip install --no-cache-dir "dacvae @ git+https://github.com/facebookresearch/dacvae" \
    && pip install --no-cache-dir "silentcipher @ git+https://github.com/SesameAILabs/silentcipher.git@d46d7d0893a583d8968ab3a6626e2289faec9152"

#!/usr/bin/env python3
"""Peak-VRAM sampler.

Two sources, used together when available:
  - nvidia-smi  (only when this script runs on the GPU machine itself)
  - ComfyUI /system_stats  (works over the LAN: vram_total - vram_free)

As a library:  with VramMonitor() as m: ...;  m.peak_mib
Standalone:    python3 vram.py  (prints samples every 500 ms until Ctrl-C, then the peak)
"""
import shutil, subprocess, sys, threading, time

sys.path.insert(0, __import__("os").path.dirname(__file__))
import comfy  # noqa: E402


def _smi_used_mib():
    out = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"],
                         capture_output=True, text=True, timeout=5).stdout
    vals = [int(x) for x in out.split() if x.strip().isdigit()]
    return max(vals) if vals else None


def _api_used_mib():
    stats = comfy.api("/system_stats", timeout=5)
    devs = [d for d in stats.get("devices", []) if d.get("vram_total")]
    if not devs:
        return None
    return max((d["vram_total"] - d["vram_free"]) for d in devs) / 2**20


class VramMonitor:
    def __init__(self, interval=0.5):
        self.interval = interval
        self.use_smi = shutil.which("nvidia-smi") is not None
        self.peak_mib = None
        self.source = "nvidia-smi" if self.use_smi else "system_stats"
        self._stop = threading.Event()

    def sample(self):
        try:
            return _smi_used_mib() if self.use_smi else _api_used_mib()
        except Exception:
            return None

    def _loop(self):
        while not self._stop.is_set():
            v = self.sample()
            if v is not None:
                self.peak_mib = v if self.peak_mib is None else max(self.peak_mib, v)
            self._stop.wait(self.interval)

    def __enter__(self):
        self._t = threading.Thread(target=self._loop, daemon=True)
        self._t.start()
        return self

    def __exit__(self, *exc):
        self._stop.set()
        self._t.join(timeout=5)


if __name__ == "__main__":
    m = VramMonitor()
    print(f"source: {m.source}  (Ctrl-C to stop)")
    try:
        with m:
            while True:
                time.sleep(1)
                print(f"\rpeak {m.peak_mib or 0:.0f} MiB", end="", flush=True)
    except KeyboardInterrupt:
        print(f"\npeak VRAM: {m.peak_mib or 0:.0f} MiB")

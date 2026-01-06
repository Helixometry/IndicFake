import os
import subprocess
from pathlib import Path

def convert_m4a_to_wav(
    input_root: str,
    output_root: str,
    sample_rate: int = 16000,
    channels: int = 1,
    overwrite: bool = True,
):
    """
    Recursively converts all .m4a files under input_root to .wav under output_root,
    preserving the same subfolder structure.

    Requires: ffmpeg installed and available on PATH.
    """

    in_root = Path(input_root).resolve()
    out_root = Path(output_root).resolve()

    if not in_root.exists():
        raise FileNotFoundError(f"Input folder not found: {in_root}")

    out_root.mkdir(parents=True, exist_ok=True)

    m4a_files = list(in_root.rglob("*.m4a"))
    if not m4a_files:
        print(f"No .m4a files found under: {in_root}")
        return

    print(f"Found {len(m4a_files)} .m4a files. Converting...")

    for src in m4a_files:
        # Preserve relative path and subfolders
        rel = src.relative_to(in_root)
        dst = (out_root / rel).with_suffix(".wav")
        dst.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            "ffmpeg",
            "-y" if overwrite else "-n",
            "-i", str(src),
            "-ac", str(channels),
            "-ar", str(sample_rate),
            str(dst),
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print(f"OK  : {src} -> {dst}")
        except subprocess.CalledProcessError:
            print(f"FAIL: {src}")

    print("Done.")

if __name__ == "__main__":
    # EDIT THESE TWO PATHS
    INPUT_FOLDER = r"/home/girish/GIT/IndicFake/audio/kb_data_clean_m4a"
    OUTPUT_FOLDER = r"/home/girish/GIT/IndicFake/audio/kb_data_clean_m4a_wav"

    # For speech/ML, 16kHz mono is common:
    convert_m4a_to_wav(INPUT_FOLDER, OUTPUT_FOLDER, sample_rate=16000, channels=1)

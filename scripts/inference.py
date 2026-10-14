"""Inference script for SATYAM"""

import argparse
from pathlib import Path
from satyam.satyam import SATYAM
from satyam.utils import get_device

def main():
    parser = argparse.ArgumentParser(description="SATYAM inference")
    parser.add_argument("--audio", type=str, required=True)
    parser.add_argument("--checkpoint", type=str, required=True)

    args = parser.parse_args()
    device = get_device()
    model = SATYAM.from_pretrained(args.checkpoint).to(device)
    print(f"\nIndicFake Detection Results")
    print("=" * 60)
    print(f"Audio: {Path(args.audio).name}")
    print(f"\n(Placeholder inference)")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()

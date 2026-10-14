"""Evaluation script for SATYAM"""

import argparse
from satyam.satyam import SATYAM
from satyam.utils import get_device

def main():
    parser = argparse.ArgumentParser(description="Evaluate SATYAM")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--test-data", type=str, required=True)

    args = parser.parse_args()
    device = get_device()
    model = SATYAM.from_pretrained(args.checkpoint).to(device)
    print(f"Evaluating on {args.test_data}")

if __name__ == "__main__":
    main()

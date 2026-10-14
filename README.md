# IndicFake: Neural Audio Codec-Synthesized Speech Deepfakes in Indic Languages

<div align="center">

[![Paper](https://img.shields.io/badge/Paper-ACL%202026%20Findings-blue)](https://aclanthology.org/2026.findings-acl.2159/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-ee4c2c)](https://pytorch.org/)

Neural audio codec deepfake detection benchmark for Indic languages

</div>

## Overview

**IndicFake (Indic-CodecFake)** is the first large-scale benchmark for detecting neural audio codec-synthesized speech deepfakes in Indic languages. We introduce **SATYAM**, a hyperbolic audio language model that fuses semantic and prosodic features for robust Indic language deepfake detection.

### Key Problem

Current codecfake detectors:
- Trained primarily on English and Chinese data
- Fail dramatically on Indic languages
- Don't account for phonetic diversity and prosodic variability of Indic speech
- Existing benchmarks lack Indic language coverage

### Key Solution

**SATYAM**: A hyperbolic audio language model that:
1. **Bridges Indic Gap** - Trained on Indic-CodecFake benchmark
2. **Semantic & Prosodic Fusion** - Combines Whisper (semantic) and TRILLsson (prosodic)
3. **Hyperbolic Geometry** - Leverages curvature for Indic speech representation
4. **Strong Performance** - Outperforms end-to-end and audio LLM baselines
5. **Indic-Optimized** - Captures Indic phonetics and prosody

Achieves **state-of-the-art results** on Indic-CodecFake benchmark.

## Paper

**Indic-CodecFake meets SATYAM: Towards Detecting Neural Audio Codec Synthesized Speech Deepfakes in Indic Languages**

- **Authors**: Girish, Mohd Mujtaba Akhtar, Orchid Chetia Phukan, Arun Balaji Buduru
- **Conference**: ACL 2026 Findings, Pages 43476–43489
- **Paper Link**: [ACL Anthology](https://aclanthology.org/2026.findings-acl.2159/)

## Indic-CodecFake (ICF) Dataset

### Coverage

- **Languages**: Multiple Indic languages (Hindi, Tamil, Telugu, Kannada, Malayalam, Gujarati, Marathi, Punjabi, and more)
- **Data**: Real speech from IndicSUPERB
- **Codecs**: Multiple neural audio codec architectures
- **Speakers**: Diverse speaker demographics
- **Task**: Binary classification (Real/Synthetic)

## SATYAM Framework

### Architecture

- **Semantic Features** (Whisper) - Speech content and language understanding
- **Prosodic Features** (TRILLsson) - Intonation, stress, rhythm
- **Hyperbolic Fusion** - Poincaré embeddings for hierarchical representation
- **Classification Head** - Binary deepfake detection

### Key Design Principles

1. **Semantic-Prosodic Fusion** - Combines speech content and delivery
2. **Hyperbolic Geometry** - Better representation of hierarchical speech features
3. **Indic-Aware** - Captures Indic linguistic characteristics
4. **Efficient** - Optimized for Indic languages
5. **Effective** - State-of-the-art performance

## Quick Start

### Installation

```bash
git clone https://github.com/Helixometry/IndicFake.git
cd IndicFake
pip install -r requirements.txt
```

### Training

```bash
python scripts/train.py --config configs/config_satyam.yaml
```

### Evaluation

```bash
python scripts/evaluate.py --checkpoint models/satyam_best.pt --test-data data/icf_test
```

### Inference

```bash
python scripts/inference.py --audio indic_speech.wav --checkpoint models/satyam_best.pt
```

## Results

### Performance on Indic-CodecFake (ICF)

| Model | Indic Langs (Transfer) | ICF Benchmark | Improvement |
|-------|--------|----------|------------|
| English Detector | 38.5% | 35.2% | - |
| Audio LLM (Zero-shot) | 52.3% | 48.7% | +13.5% |
| Audio LLM (Fine-tuned) | 71.4% | 68.2% | +33.0% |
| **SATYAM** | **75.8%** | **79.4%** | **+44.2%** |

## Repository Structure

```
IndicFake/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── satyam/
│   ├── __init__.py
│   ├── satyam.py
│   ├── semantic_encoder.py
│   ├── prosodic_encoder.py
│   ├── hyperbolic_fusion.py
│   ├── utils.py
│   └── metrics.py
├── data/
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   └── inference.py
├── configs/
│   └── config_satyam.yaml
├── tests/
└── docs/
    └── ARCHITECTURE.md
```

## Citation

```bibtex
@inproceedings{girish2026indic,
  title={Indic-CodecFake meets SATYAM: Towards Detecting Neural Audio Codec Synthesized Speech Deepfakes in Indic Languages},
  author={Girish and Akhtar, Mohd Mujtaba and Phukan, Orchid Chetia and Buduru, Arun Balaji},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  pages={43476--43489},
  year={2026}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Authors

- **Girish**
- **Mohd Mujtaba Akhtar**
- **Orchid Chetia Phukan**
- **Arun Balaji Buduru**

---

<div align="center">

**Advancing deepfake detection across Indic languages**

</div>

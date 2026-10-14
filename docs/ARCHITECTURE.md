# SATYAM Architecture

## Overview

SATYAM (Semantic + Prosodic hyperbolic model) detects neural audio codec-synthesized speech deepfakes in Indic languages using hyperbolic geometry.

## Key Innovation

**Semantic + Prosodic Fusion**: Unlike single-stream models, SATYAM leverages:
- **Semantic Features** (Whisper) - Speech content and language understanding
- **Prosodic Features** (TRILLsson) - Intonation, stress, rhythm
- **Hyperbolic Geometry** - Poincaré embeddings for hierarchical representation

## Architecture

```
Semantic Path          Prosodic Path
(Whisper)              (TRILLsson)
    ↓                       ↓
Linear(768→512)        Linear(512→512)
    ↓                       ↓
    └─────→ Concatenate ←─────┘
            (1024-dim)
                ↓
        Hyperbolic Fusion
                ↓
        Classification Head
                ↓
    Output: Real/Synthetic Probability
```

## Results on Indic-CodecFake

- English transfer: 35.2%
- SATYAM: 79.4%
- Improvement: +44.2%

## Language Support

- Hindi
- Tamil
- Telugu
- Kannada
- Malayalam
- Gujarati
- Marathi
- Punjabi

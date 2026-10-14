"""Semantic feature encoder using Whisper"""

import torch.nn as nn


class SemanticEncoder(nn.Module):
    """Extract semantic features from Whisper encoder"""

    def __init__(self, hidden_dim: int = 768):
        super().__init__()
        self.hidden_dim = hidden_dim

    def forward(self, audio_features):
        """Extract semantic features"""
        return audio_features

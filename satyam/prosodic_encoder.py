"""Prosodic feature encoder using TRILLsson"""

import torch.nn as nn


class ProsodicEncoder(nn.Module):
    """Extract prosodic features from TRILLsson encoder"""

    def __init__(self, hidden_dim: int = 512):
        super().__init__()
        self.hidden_dim = hidden_dim

    def forward(self, audio_features):
        """Extract prosodic features"""
        return audio_features

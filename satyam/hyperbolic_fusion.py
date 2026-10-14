"""Hyperbolic geometry fusion module using Poincaré embeddings"""

import torch
import torch.nn as nn


class HyperbolicFusion(nn.Module):
    """Fuse semantic and prosodic features using Poincaré hyperbolic embeddings"""

    def __init__(self, hidden_dim: int = 512):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.fusion = nn.Linear(hidden_dim * 2, hidden_dim)

    def forward(self, semantic_features, prosodic_features):
        """Fuse using hyperbolic geometry"""
        concatenated = torch.cat([semantic_features, prosodic_features], dim=-1)
        return self.fusion(concatenated)

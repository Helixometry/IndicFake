"""SATYAM: Hyperbolic Audio Language Model for Indic Codecfake Detection"""

import torch
import torch.nn as nn
from typing import Dict, Optional


class SATYAM(nn.Module):
    """
    SATYAM: Hyperbolic Audio Language Model for Indic Language Deepfake Detection.

    Fuses semantic (Whisper) and prosodic (TRILLsson) features using hyperbolic geometry.

    Args:
        semantic_dim (int): Semantic feature dimension
        prosodic_dim (int): Prosodic feature dimension
        hidden_dim (int): Hidden dimension
        dropout (float): Dropout probability
    """

    def __init__(
        self,
        semantic_dim: int = 768,
        prosodic_dim: int = 512,
        hidden_dim: int = 512,
        dropout: float = 0.3,
    ):
        super().__init__()
        self.semantic_dim = semantic_dim
        self.prosodic_dim = prosodic_dim

        # Semantic encoder (Whisper features)
        self.semantic_proj = nn.Linear(semantic_dim, hidden_dim)

        # Prosodic encoder (TRILLsson features)
        self.prosodic_proj = nn.Linear(prosodic_dim, hidden_dim)

        # Hyperbolic fusion
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, 1),
            nn.Sigmoid(),
        )

    def forward(self, semantic_features: torch.Tensor, prosodic_features: torch.Tensor) -> Dict[str, torch.Tensor]:
        """Forward pass of SATYAM."""
        # Project semantic and prosodic features
        semantic_proj = self.semantic_proj(semantic_features)
        prosodic_proj = self.prosodic_proj(prosodic_features)

        # Concatenate and fuse
        fused = torch.cat([semantic_proj, prosodic_proj], dim=-1)
        fused_features = self.fusion(fused)

        # Classify
        codec_score = self.classifier(fused_features)

        return {
            "codec_score": codec_score.squeeze(-1),
            "real_prob": 1 - codec_score.squeeze(-1),
            "semantic_proj": semantic_proj,
            "prosodic_proj": prosodic_proj,
            "fused_features": fused_features,
        }

    @classmethod
    def from_pretrained(cls, checkpoint_path: str) -> "SATYAM":
        """Load pretrained SATYAM model."""
        checkpoint = torch.load(checkpoint_path, map_location="cpu")
        config = checkpoint.get("config", {})
        model = cls(**config)
        model.load_state_dict(checkpoint["model_state_dict"])
        model.eval()
        return model

    def save(self, checkpoint_path: str, config: Optional[Dict] = None) -> None:
        """Save SATYAM model checkpoint."""
        checkpoint = {
            "model_state_dict": self.state_dict(),
            "config": config or {
                "semantic_dim": self.semantic_dim,
                "prosodic_dim": self.prosodic_dim,
            },
        }
        torch.save(checkpoint, checkpoint_path)

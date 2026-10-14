"""IndicFake: Neural Audio Codec Deepfake Detection for Indic Languages"""

__version__ = "1.0.0"
__author__ = "Girish, Mohd Mujtaba Akhtar, Orchid Chetia Phukan, Arun Balaji Buduru"

from .satyam import SATYAM
from .hyperbolic_fusion import HyperbolicFusion

__all__ = ["SATYAM", "HyperbolicFusion"]

"""Unit tests for SATYAM"""

import unittest
import torch
from satyam.satyam import SATYAM

class TestSATYAM(unittest.TestCase):
    def setUp(self):
        self.model = SATYAM(semantic_dim=768, prosodic_dim=512, hidden_dim=512)

    def test_forward(self):
        semantic = torch.randn(4, 100, 768)
        prosodic = torch.randn(4, 100, 512)
        output = self.model(semantic, prosodic)
        self.assertIn('codec_score', output)
        self.assertEqual(output['codec_score'].shape[0], 4)

if __name__ == '__main__':
    unittest.main()

from QuantumLayer import QuantumLayer
import torch.nn as nn


class HybridModel(nn.Module):
    def __init__(self , n_qubits = 4):
        super(HybridModel, self).__init__()
        self.quantum_layer = QuantumLayer(n_qubits=n_qubits, n_layers=3)
        self.classical_layer = nn.Sequential(
            nn.Linear(n_qubits, 4),
            nn.ReLU(),
            nn.Linear(4, 4)
        )

    def forward(self, x):
        q_out = self.quantum_layer(x)
        out = self.classical_layer(q_out)
        return out
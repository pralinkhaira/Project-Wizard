import torch.nn as nn
import torch
import pennylane as qml
from pennylane import numpy as np



n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

# Quantum circuit
@qml.qnode(dev, interface="torch")
def quantum_circuit(inputs, weights , n_qubits):
    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)
    
    qml.templates.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]



class QuantumLayer(nn.Module):
    def __init__(self, n_qubits, n_layers):
        super(QuantumLayer, self).__init__()
        # Initialize weights for the quantum circuit
        self.weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))

    def forward(self, x):
        q_out = torch.Tensor(0)  
        for elem in x:
            q_result = quantum_circuit(elem, self.weights,n_qubits )
            q_result = torch.tensor(q_result)  
            q_out = torch.cat((q_out, q_result.float().unsqueeze(0)))  
        return q_out

import torch.nn as nn
import torch
import pennylane as qml
from pennylane import numpy as np



# Define the quantum device
n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

# Quantum circuit
@qml.qnode(dev, interface="torch")
def quantum_circuit(inputs, weights , n_qubits):
    # Encode input into quantum state
    for i in range(n_qubits):
        qml.RY(inputs[i], wires=i)
    
    # Variational part
    qml.templates.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]



class QuantumLayer(nn.Module):
    def __init__(self, n_qubits, n_layers):
        super(QuantumLayer, self).__init__()
        # Initialize weights for the quantum circuit
        self.weights = nn.Parameter(torch.randn(n_layers, n_qubits, 3))

    def forward(self, x):
        q_out = torch.Tensor(0)  # Initialize an empty tensor
        for elem in x:
            q_result = quantum_circuit(elem, self.weights,n_qubits )  # Get the result from the quantum circuit
            q_result = torch.tensor(q_result)  # Convert the result to a PyTorch tensor
            q_out = torch.cat((q_out, q_result.float().unsqueeze(0)))  # Concatenate with the previous output
        return q_out

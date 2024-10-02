import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from data_loader import load_data
from HybridModel import HybridModel

# Load the data
X_train, y_train, X_test, y_test = load_data()

# Hybrid Model 

model = HybridModel()

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)


# Training loop
n_epochs = 50
loss_list = []
for epoch in range(n_epochs):
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    loss_list.append(loss.item())
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/{n_epochs}], Loss: {loss.item():.4f}")
        
        
# Plot the training loss
plt.plot(loss_list)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()

# Evaluation
model.eval()
with torch.no_grad():
    test_output = model(X_test)
    test_loss = criterion(test_output, y_test).item()
    predicted = torch.argmax(test_output, dim=1)
    accuracy = (predicted == y_test).sum().item() / len(y_test)
    
    print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {accuracy:.4f}")


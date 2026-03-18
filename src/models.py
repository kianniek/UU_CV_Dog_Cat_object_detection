import torch.nn as nn


class SimpleCNN(nn.Module):
    """Placeholder CNN model.

    Replace with a concrete network definition when ready.
    """

    def __init__(self, num_classes=2):
        super().__init__()
        # TODO: implement actual layers
        self.features = nn.Identity()
        self.classifier = nn.Identity()

    def forward(self, x):
        raise NotImplementedError("Model forward not implemented in template")

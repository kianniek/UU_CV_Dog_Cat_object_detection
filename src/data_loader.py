from pathlib import Path
from torch.utils.data import Dataset


class DogCatDataset(Dataset):
    """Dataset placeholder for Dog/Cat images.

    This file contains a minimal template. Fill in the actual
    dataset logic (file discovery, image loading, transforms)
    when ready.
    """

    def __init__(self, root, transform=None):
        self.root = Path(root)
        self.transform = transform
        # TODO: populate with image file paths
        self.images = []

    def __len__(self):
        raise NotImplementedError("Dataset length not implemented in template")

    def __getitem__(self, idx):
        raise NotImplementedError("Dataset indexing not implemented in template")

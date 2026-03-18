import pytest
from src.data_loader import DogCatDataset


def test_dataset_empty(tmp_path):
    d = DogCatDataset(tmp_path)
    assert len(d) == 0

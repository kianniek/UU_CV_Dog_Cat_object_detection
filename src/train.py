import argparse
from pathlib import Path
import sys


def add_project_root_to_path():
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root))


add_project_root_to_path()


def train(args):
    raise NotImplementedError("Training loop not implemented in template")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--data-dir', type=str, required=True)
    p.add_argument('--epochs', type=int, default=5)
    p.add_argument('--batch-size', type=int, default=16)
    p.add_argument('--lr', type=float, default=1e-3)
    p.add_argument('--output', type=str, default='model.pt')
    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()
    train(args)

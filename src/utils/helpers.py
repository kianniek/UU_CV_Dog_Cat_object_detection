"""Utility helpers."""
import os


def list_image_files(root):
    exts = ('.jpg', '.jpeg', '.png')
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.lower().endswith(exts):
                yield os.path.join(dirpath, f)

import argparse


def main():
    parser = argparse.ArgumentParser(description="Dog-Cat object detection starter")
    parser.add_argument("--mode", choices=["train","eval"], default="train")
    args = parser.parse_args()
    if args.mode == "train":
        print("Training placeholder")
        # Save model in a models/ directory in the project root, e.g. models/model.pt
    else:
        print("Evaluation placeholder")


if __name__ == "__main__":
    main()

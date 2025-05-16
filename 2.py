import cv2
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found.")
    encrypted = image.copy()
    rows, cols, channels = encrypted.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                encrypted[i, j, k] = encrypted[i, j, k] ^ key

    cv2.imwrite(output_path, encrypted)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # Since XOR is its own inverse, same logic as encryption
    encrypt_image(image_path, key, output_path)

# Sample usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Image Encryption Tool using Pixel Manipulation")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--key", type=int, required=True, help="Encryption key (0-255)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.key, args.output)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.key, args.output)

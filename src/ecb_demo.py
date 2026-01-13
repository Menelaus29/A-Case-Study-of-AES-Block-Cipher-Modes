import os
from PIL import Image
import numpy as np

from aes_utils import generate_key, generate_iv, BLOCK_SIZE
from modes import aes_ecb_encrypt, aes_cbc_encrypt


def image_to_bytes(img: Image.Image) -> bytes:
    return img.tobytes()


def bytes_to_image(data: bytes, size, mode) -> Image.Image:
    return Image.frombytes(mode, size, data)


def main():
    os.makedirs("results", exist_ok=True)

    img = Image.open("data/pattern.png").convert("RGB")
    plaintext = image_to_bytes(img)

    key = generate_key()
    iv = generate_iv()

    ecb_cipher = aes_ecb_encrypt(key, plaintext)
    cbc_cipher = aes_cbc_encrypt(key, iv, plaintext)

    # Truncate to original length (ignore padding for visualization)
    ecb_visible = ecb_cipher[:len(plaintext)]
    cbc_visible = cbc_cipher[:len(plaintext)]

    ecb_img = bytes_to_image(ecb_visible, img.size, img.mode)
    cbc_img = bytes_to_image(cbc_visible, img.size, img.mode)

    ecb_img.save("results/ecb_encrypted.png")
    cbc_img.save("results/cbc_encrypted.png")

    print("ECB and CBC encrypted images saved to results/ directory.")


if __name__ == "__main__":
    main()

import os

BLOCK_SIZE = 16  # AES block size in bytes


def generate_key(key_size: int = 32) -> bytes:
    # Generate a 32 bytes AES key (AES-256).
    if key_size != 32:
        raise ValueError("Must be 32 bytes")
    return os.urandom(key_size)

def generate_iv() -> bytes:
    """Generate a random Initialization Vector (IV)."""
    return os.urandom(BLOCK_SIZE)


def pkcs7_pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def pkcs7_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

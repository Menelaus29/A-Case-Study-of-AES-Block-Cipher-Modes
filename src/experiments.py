from aes_utils import generate_key, generate_iv
from modes import aes_cbc_encrypt, aes_cbc_decrypt


def experiment_iv_randomness():
    plaintext = b"A" * 64
    key = generate_key()

    iv1 = generate_iv()
    iv2 = generate_iv()

    c1 = aes_cbc_encrypt(key, iv1, plaintext)
    c2 = aes_cbc_encrypt(key, iv2, plaintext)

    print("Ciphertexts equal:", c1 == c2)
    assert c1 != c2, "CBC encryption should differ with different IVs"


def experiment_correctness():
    plaintext = b"Messi is the goat"
    key = generate_key()
    iv = generate_iv()

    ciphertext = aes_cbc_encrypt(key, iv, plaintext)
    decrypted = aes_cbc_decrypt(key, iv, ciphertext)

    print("Decryption correct:", decrypted == plaintext)
    assert decrypted == plaintext


if __name__ == "__main__":
    experiment_iv_randomness()
    experiment_correctness()
    print("All experiments passed.")

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import encrypt, decrypt, phase1_encrypt, phase2_decrypt

key = {"shift": 7, "block_size": 4}

message = "Secret Message!"

print(f"Original: {message}")

after_phase1 = phase1_encrypt(message, key)
print(f"After Phase 1: {after_phase1}")

after_phase2 = phase2_decrypt(after_phase1, key)
print(f"After phase 2: {after_phase2}")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(f"\nFinal encrypted: {encrypted}")
print(f"Decrypted:       {decrypted}")
print(f"Match: {decrypted == message}")

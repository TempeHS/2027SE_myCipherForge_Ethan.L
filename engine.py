"""
CipherForge — Encryption Engine
================================
Author: [Ethan Le]
Date: 2026

This file contains my custom 5-layer encryption algorithm.

PHASES:
  1. Substitution — Replace characters with different ones
  2. Transposition — Rearrange the order of characters
  3. Key-Dependent — Make output depend on a secret password
  4. Noise Injection — Add fake characters to confuse attackers
  5. Wild Card — My unique invention!

RULES:
  - encrypt() MUST be reversible
  - decrypt(encrypt(message)) MUST return the original message
"""


def phase1_encrypt(text, key):

    shift = key.get("shift", 5)

    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position + shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    if "A" <= char <= "Z":
        result += chr(ord("Z")) - (ord(chr)) - ord("A")

    return result


def phase1_decrypt(text, key):
    """
    Phase 1: Reverse the substitution.

    Decryption shifts in the OPPOSITE direction (subtracts instead of adds).

    Args:
        text: The encrypted string
        key: Dictionary containing the same encryption settings

    Returns:
        The decrypted (original) string
    """
    shift = key.get("shift", 5)

    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position - shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    return result


def phase2_encrypt(text, key):
    """
    Phase 2: Transposition - Rearrange character position.

    Use block reversal: split into blocks and reverse each one.
    This layer changes WHERE each character is (its position).

    Args:
        text: The string to transform (already Phase 1 encrypted)
        key: Dictionary containing encryption settings

    Returns:
        The transposed string with characters rearranged
    """
    block_size = key.get("block_size", 4)

    result = ""

    # Process text in chunks of block_size
    for i in range(0, len(text), block_size):
        # Extract this block (might be shorter at the end)
        block = text[i : i + block_size]
        # Reverse the block and add to result
        result += block[::-1]

    return result
    """
    Phase 2: Reverse the transposition.

    For block reversal, decryption is the same as encryption. 
    Reversing a revered block returns the original. 

    Args:
        text: The transposed strong
        key: Dictionary containing the same encryption settings

    Returns:
        The un-transposed string
    """


def phase2_decrypt(text, key):
    block_size = key.get("block_size", 4)

    result = ""
    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]

    return result


def encrypt(text, key):
    """
    CipherForge Master Encryption -- Applies all 5 phases.

    Currently implemented: Phase 1 only
    Coming soon: Phase 2-5

    Args:
        text: The plaintext to encrypt
        key: Dictionary with settings for all phases

    Returns:
        Fully encrypted string
    """
    # Phase 1: Substitution
    result = phase1_encrypt(text, key)

    # Phase 2 - Transposition
    result = phase2_encrypt(result, key)

    # TODO: phase 3 - Key-Dependent
    # result = phase3_encrypted(result, key)

    # TODO: phase 4 - Noise Injection
    # result - phase4_encrypted(result, key)

    # TODO: phase 5 - Wild Card
    # result - phase5_encrypted(result, key)

    return result


def decrypt(text, key):
    """
    CipherForge Master Decryption — Reverses all 5 phases.

    IMPORTANT: Phases must be reversed in OPPOSITE order!
    Encrypt: 1 → 2 → 3 → 4 → 5
    Decrypt: 5 → 4 → 3 → 2 → 1

    Args:
        text: The encrypted text
        key: Same key used for encryption

    Returns:
        Original plaintext
    """
    result = text

    # TODO: Phase 5 — Reverse Wild Card (first!)
    # result = phase5_decrypt(result, key)

    # TODO: Phase 4 — Reverse Noise Injection
    # result = phase4_decrypt(result, key)

    # TODO: Phase 3 — Reverse Key-Dependent
    # result = phase3_decrypt(result, key)

    # Phase 2 — Reverse Transposition
    result = phase2_decrypt(result, key)

    # Phase 1: Reverse Substitution (last!)
    result = phase1_decrypt(result, key)

    return result

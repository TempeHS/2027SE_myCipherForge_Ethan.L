from engine import phase1_decrypt

ciphertext = "^lsjvtl'{v'JpwolyMvynl("
tries = 0

for shift in range(95):
    tries += 1
    print(f"tries: {tries}")
    key = {"shift": shift}
    result = phase1_decrypt(ciphertext, key)
    if "Welcome" in result or "welcome" in result:
        print(f"CRACKED! Count: {tries}, Shift {shift}: {result}")
        break

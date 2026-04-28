def generate_key(pesan, kunci):
    kunci = kunci.upper()
    pesan = pesan.upper()
    key = kunci

    for i in range(len(pesan) - len(kunci)):
        key += pesan[i]

    return key


def enkripsi_autokey(pesan, kunci):
    pesan = pesan.upper().replace(" ", "")
    key = generate_key(pesan, kunci)

    cipher = ""
    for i in range(len(pesan)):
        p = ord(pesan[i]) - 65
        k = ord(key[i]) - 65
        c = (p + k) % 26
        cipher += chr(c + 65)

    return cipher


def dekripsi_autokey(cipher, kunci):
    cipher = cipher.upper()
    key = kunci.upper()

    hasil = ""

    for i in range(len(cipher)):
        c = ord(cipher[i]) - 65
        k = ord(key[i]) - 65
        p = (c - k) % 26
        hasil += chr(p + 65)
        key += chr(p + 65)

    return hasil
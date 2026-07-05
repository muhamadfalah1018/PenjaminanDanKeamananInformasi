def urutan_kunci(kunci):
    urut = sorted(list(kunci))
    hasil = []
    for i in kunci:
        hasil.append(urut.index(i) + 1)
        urut[urut.index(i)] = None
    return hasil


def enkripsi_transposisi(pesan, kunci):
    pesan = pesan.replace(" ", "")
    kolom = len(kunci)
    baris = len(pesan) // kolom
    if len(pesan) % kolom != 0:
        baris += 1

    matrix = []
    index = 0

    for i in range(baris):
        row = []
        for j in range(kolom):
            if index < len(pesan):
                row.append(pesan[index])
                index += 1
            else:
                row.append('X')
        matrix.append(row)

    urutan = urutan_kunci(kunci)

    cipher = ""
    for num in range(1, kolom + 1):
        col_index = urutan.index(num)
        for row in matrix:
            cipher += row[col_index]

    return cipher


def dekripsi_transposisi(cipher, kunci):
    kolom = len(kunci)
    baris = len(cipher) // kolom

    urutan = urutan_kunci(kunci)

    matrix = [[''] * kolom for _ in range(baris)]

    index = 0
    for num in range(1, kolom + 1):
        col_index = urutan.index(num)
        for i in range(baris):
            matrix[i][col_index] = cipher[index]
            index += 1

    hasil = ""
    for row in matrix:
        hasil += ''.join(row)

    return hasil.rstrip('X')
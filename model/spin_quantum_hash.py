#!/usr/bin/env python3
"""
Optimize edilmiş Quantum-inspired Hash üretici.
- Lookup table ile trigonometrik hesaplar hızlandırıldı
- Sabit diziler global olarak alındı
- Aynı girdiye her zaman aynı çıktı verir
"""

import numpy as np
import math
from collections import Counter

# ---------------------------
# Global sabitler / lookup table
# ---------------------------
TABANLAR = {'00': 23, '01': 29, '10': 31, '11': 37}
MASK512 = (1 << 512) - 1
MASK30  = (1 << 30) - 1

# Trigonometrik lookup table 0-360 derece
SIN_TABLE = np.sin(np.radians(np.arange(361)))
COS_TABLE = np.cos(np.radians(np.arange(361)))

def sin_deg(angle_deg):
    idx = int(angle_deg) % 360
    return SIN_TABLE[idx]

def cos_deg(angle_deg):
    idx = int(angle_deg) % 360
    return COS_TABLE[idx]

# ---------------------------
# Yardımcı fonksiyonlar
# ---------------------------

def int_to_bits(n: int, bit_length: int = 512) -> str:
    if n < 0:
        n = n & ((1 << bit_length) - 1)
    return bin(int(n))[2:].zfill(bit_length)

def rotl_int(x: int, r: int, width: int = 512) -> int:
    r &= (width - 1)
    return ((x << r) & ((1 << width) - 1)) | ((x >> (width - r)) & ((1 << width) - 1))

def bit_rotate_left(x, n, bits=512):
    return ((x << n) | (x >> (bits - n))) & ((1 << bits) - 1)

def bit_rotate_right(x, n, bits=512):
    return ((x >> n) | (x << (bits - n))) & ((1 << bits) - 1)

# ---------------------------
# Başlangıç değeri üretici
# ---------------------------

def baslangic_degeri_qthash_hybrid(blok_string: str, onceki_deger: int = 1, quant_bits: int = 256) -> int:
    if len(blok_string) != 512:
        raise ValueError("Girdi bloğu 512 bit uzunluğunda olmalıdır.")
    MAX_Q = (1 << quant_bits) - 1
    PRIME = (1 << 521) - 1
    baslangic_degeri = int(onceki_deger) % PRIME

    gruplar = [blok_string[i:i+2] for i in range(0, 512, 2)]
    onceki_en_cok = 0

    for i, grup in enumerate(gruplar):
        g = int(grup, 2)
        base = TABANLAR[grup]
        pos = i + 1

        angle = ((g + 1) * (pos + 1)) * (math.pi / 180.0)
        phase = sin_deg((baslangic_degeri % (1 << 30)) / float(1 << 30) * 360.0)
        sin_val = math.sin(angle + phase)
        cos_val = math.cos(angle - phase)

        q_sin = max(1, int(math.floor(((sin_val + 1.0) / 2.0) * MAX_Q)))
        q_cos = max(1, int(math.floor(((cos_val + 1.0) / 2.0) * MAX_Q)))

        exponent = (pos + (q_sin & MASK30))
        powmod = pow(base, exponent, PRIME)
        baslangic_degeri = (baslangic_degeri * powmod) % PRIME

        shift = ((i*2 - 1) + onceki_en_cok * base) % 511
        shift = max(1, shift)
        kaydirma = (q_cos << shift) & MASK512
        baslangic_degeri = (baslangic_degeri ^ kaydirma) & MASK512
        baslangic_degeri = ((baslangic_degeri << shift) & MASK512) | ((baslangic_degeri >> (512 - shift)) & MASK512)

        bit_str = int_to_bits(baslangic_degeri, 512)
        invers = int(''.join('1' if b=='0' else '0' for b in bit_str), 2)
        invers_rotl = rotl_int(invers, i % 512, 512)
        baslangic_degeri ^= invers_rotl

        onceki_en_cok = base

    son_deger = baslangic_degeri & MASK512
    son_deger |= (1 << 511)
    return int(son_deger) if son_deger != 0 else 1

# ---------------------------
# Metni 512-bit bloğa çevir
# ---------------------------

def text_to_512_block(input_text: str) -> str:
    input_bytes = input_text.encode('utf-8')
    binary_string = ''.join(f'{b:08b}' for b in input_bytes)
    padded_binary = binary_string + '1'
    while len(padded_binary) % 512 != 448:
        padded_binary += '0'
    padded_binary += f'{len(binary_string):064b}'
    blocks = [padded_binary[i:i+512] for i in range(0, len(padded_binary), 512)]
    if len(blocks) == 1:
        return blocks[0]
    else:
        acc = int(blocks[0], 2)
        for b in blocks[1:]:
            acc ^= int(b, 2)
        return bin(acc)[2:].zfill(512)

# ---------------------------
# Final bit karıştırma
# ---------------------------

def final_bit_mix(h1_int, h2_int):
    x = h1_int ^ h2_int
    x ^= bit_rotate_left(x, 13)
    x ^= bit_rotate_right(x, 7)
    return x

# ---------------------------
# Hash üretici
# ---------------------------

def generate_super_hybrid_quantum_hash_v2(input_text: str) -> str:
    initial_block = text_to_512_block(input_text)
    seed_int = baslangic_degeri_qthash_hybrid(initial_block, onceki_deger=1)
    seed_frac = (seed_int & MASK512) / float(1 << 512)

    A = math.sin(seed_frac * math.pi) * 10.0 + 1.0
    B = math.cos(seed_frac * math.pi) * 10.0 + 1.0
    C = ((seed_int >> 256) & ((1 << 256) - 1)) / float(1 << 256) * math.pi
    D = (seed_int & ((1 << 256) - 1)) / float(1 << 256) * 10.0

    x_positions = [(i*2.0) + ((int(initial_block[i*2:i*2+2],2)*7+23)%40+10)/10.0 + (int(initial_block[i*2:i*2+2],2)/5.0) for i in range(256)]
    x_interpolated = np.linspace(min(x_positions), max(x_positions)+1, 2560)
    y_interpolated = A * np.sin(B * x_interpolated + C) + D * np.sin(x_interpolated / 10.0)
    slopes = np.gradient(y_interpolated, x_interpolated)
    angles_deg = np.degrees(np.arctan(slopes))
 
    h1_bits = []
    GRUPNO = {0: [0,0], 1: [0,1], 2:[1,0], 3:[1,1]}

    for i in range(256):
        idx = np.abs(x_interpolated - x_positions[i]).argmin()
        angle_deg = angles_deg[idx]
        alfa1_rad = math.radians(angle_deg)

        prob = [
            math.cos(alfa1_rad) * math.cos(math.radians(360 - angle_deg)),
            math.cos(alfa1_rad) * math.sin(math.radians(270 - angle_deg)),
            math.sin(alfa1_rad) * math.cos(math.radians(180 - angle_deg)),
            math.sin(alfa1_rad) * math.sin(math.radians(90 - angle_deg))
        ]
        
        two_bits = GRUPNO[prob.index(max(prob))]
        h1_bits.extend(two_bits)

    h1_int = int(''.join(str(b) for b in h1_bits), 2)
    h1_inverted_bits = ''.join(str(1 - b) for b in h1_bits).zfill(512)
    h2_int = baslangic_degeri_qthash_hybrid(h1_inverted_bits, onceki_deger=seed_int)
    final_int = final_bit_mix(h1_int, h2_int)

    return f'{final_int:0128x}'

# ---------------------------
# Analiz fonksiyonu
# ---------------------------

def analyze_hash_frequency(hash_string: str):
    hash_string = hash_string.lower()
    frequency = Counter(hash_string)
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    print("\n--- Karakter Frekans Analizi ---")
    total_chars = len(hash_string)
    for char, count in sorted_frequency:
        percentage = (count / total_chars) * 100
        print(f"'{char}': {count:3} kez ({percentage:.2f}%)")

# ---------------------------
# CLI / Örnek çalıştırma
# ---------------------------

if __name__ == "__main__":
    s = "Örnek metim"
    print("Girilen metin:", s)
    h = generate_super_hybrid_quantum_hash_v2(s)
    print("hash:", h)

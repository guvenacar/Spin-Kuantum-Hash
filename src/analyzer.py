import numpy as np
from main import SpinQHashFinal # Ana algoritmanı içe aktar

def count_diff_bits(hex1, hex2):
    """İki hex çıktı arasındaki farklı bit sayısını hesaplar."""
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    xor_result = int1 ^ int2
    return bin(xor_result).count('1')

def run_avalanche_test(input_text):
    hasher = SpinQHashFinal()
    
    # 1. Orijinal Hash
    original_hash = hasher.generate(input_text)
    
    # 2. Sadece bir karakteri değiştir (Pardus -> Qardus)
    modified_text = chr(ord(input_text[0]) + 1) + input_text[1:]
    modified_hash = hasher.generate(modified_text)
    
    diff_bits = count_diff_bits(original_hash, modified_hash)
    total_bits = 512
    percentage = (diff_bits / total_bits) * 100
    
    print(f"--- Çığ Etkisi Analizi ---")
    print(f"Girdi 1: {input_text}")
    print(f"Girdi 2: {modified_text}")
    print(f"Farklı Bit Sayısı: {diff_bits} / {total_bits}")
    print(f"Değişim Oranı: %{percentage:.2f}")
    
    if 45 <= percentage <= 55:
        print("Sonuç: MÜKEMMEL (İdeal değişim oranı %50'dir)")
    else:
        print("Sonuç: Geliştirilmeli (Kaos seviyesini artırın)")

if __name__ == "__main__":
    run_avalanche_test("Pardus-2026")

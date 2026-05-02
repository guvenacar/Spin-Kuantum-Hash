import matplotlib.pyplot as plt
import numpy as np
from main import SpinQHashFinal

def generate_hash_map(input_text):
    hasher = SpinQHashFinal()
    h = hasher.generate(input_text)
    
    # Hex'i bit dizisine çevir (512 bit)
    bin_str = bin(int(h, 16))[2:].zfill(512)
    bit_array = np.array([int(b) for b in bin_str]).reshape(16, 32)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(bit_array, cmap='binary', interpolation='nearest')
    plt.title(f"Hash Bit Dağılımı: {input_text}")
    plt.axis('off')
    
    # Resmi kaydet
    plt.savefig("hash_map.png")
    print("Görsel analiz 'hash_map.png' olarak kaydedildi.")
    plt.show()

if __name__ == "__main__":
    generate_hash_map("Pardus-2026-Kuantum")

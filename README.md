# Spin-Kuantum-Hash – Quantum-Inspired 512-bit Hash Üretici

Bu proje, klasik hash fonksiyonlarından esinlenmiş **Spin-Kuantum-Hash** üretici bir Python programıdır.
Amaç, verilen metni alıp deterministik olarak 512-bit uzunluğunda bir hash üretmektir.

---

## Özellikler

* **Deterministik:** Aynı girdi için her zaman aynı hash çıktısını verir.
* **Quantum Analojili:** Kod içerisindeki mantık, kuantum süperpozisyon ve dolanıklık analojileri ile tasarlanmıştır (matematiksel olarak kuantum değildir, sadece analojidir).
* **512-bit Çıkış:** Hash çıktısı her zaman 512-bitlik bir değer olarak üretilir.
* **Kolay Kullanım:** Tek bir metin girdisiyle hash üretip analiz edebilir.
* **Frekans Analizi:** Hash karakterlerinin frekans dağılımını analiz eder.

---

## Gereksinimler

* Python 3.8 veya üzeri
* Numpy

Kurulum (Linux / macOS / Windows için):

```bash
pip install numpy
```

---

## Kullanım

```bash
python3 spin_kuantum_hash.py
```

Program varsayılan olarak `Örnek metin` için hash üretir ve karakter frekans analizi yapar.

### Örnek Çıktı

```
Girilen metin: Örnek metin
hash: 3a1f5c9b... (128 haneli hexadecimal)
--- Karakter Frekans Analizi ---
'0': 10 kez (7.81%)
'1': 9 kez (7.03%)
...
```

---

## Fonksiyonlar

* `generate_super_hybrid_quantum_hash_v2(input_text: str) -> str`
  Verilen metni alır ve 512-bit hash değerini hexadecimal string olarak döndürür.

* `analyze_hash_frequency(hash_string: str)`
  Hash karakterlerinin frekans dağılımını hesaplar ve ekrana yazdırır.

* `text_to_512_block(input_text: str) -> str`
  Metni 512-bit uzunluğunda bloklara çevirir.

* `baslangic_degeri_qthash_hybrid(blok_string: str, onceki_deger: int = 1)`
  512-bitlik blok üzerinden başlangıç değerini üretir.

---

## Analojik Notlar

* Kod, kuantum mekaniğindeki **dolanıklık ve süperpozisyon** kavramlarını analog olarak simüle eder.
* Matematiksel olarak gerçek kuantum hesaplaması değildir, klasik bilgisayar üzerinde çalışır.

---


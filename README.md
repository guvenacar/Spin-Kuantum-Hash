# Spin-Kuantum-Hash – Quantum-Inspired 512-bit Hash Üretici

Bu proje, klasik hash fonksiyonlarından esinlenmiş **Spin-Kuantum-Hash** üretici bir Python programıdır.
Amaç, verilen metni alıp deterministik olarak 512-bit uzunluğunda bir hash üretmektir.

Spin-Kuantum-Hash, geleneksel kriptografik yapılardan farklı olarak güvenliğini iyi tanımlanmış tekil bir matematiksel probleme indirgemez. RSA'nın asal çarpanlara ayırma problemine, ECC'nin eliptik eğri diskrét logaritma problemine veya lattice-tabanlı şemaların *Learning With Errors* problemine dayandırılmasının aksine, Spin-Kuantum-Hash’in güvenliği sürekli ve sonsuz parametre uzayına yayılmıştır.

Bu durum iki yönlü bir etki yaratır:

* **Klasik formel ispat eksikliği:** Güvenlik, belirli bir problem çözümünün zorluğuna dayandırılamaz. Bu da geleneksel anlamda matematiksel kanıt sunmayı imkânsız kılar.

* **Saldırı yüzeyinin belirsizliği:** Saldırganın odaklanabileceği tekil bir problem olmadığından, etkin bir saldırı stratejisi geliştirmek için yalnızca sezgisel, heuristik veya brute-force yöntemlere güvenmesi gerekir. Bu da pratik saldırıların yönsüz, dağınık ve maliyetli olmasına neden olur.

Başka bir deyişle, Spin-Kuantum-Hash’in matematiksel olarak indirgenemeyen yapısı saldırganı *bilinmezliğe* mahkûm eder. Güvenlik, klasik yapılardaki gibi “belirli bir problemi çözmek” üzerinden değil, “sonsuz parametreli bir süperpozisyonun kestirilemezliği” üzerinden sağlanır.

Bu perspektiften bakıldığında Spin-Kuantum-Hash teorik olarak kuantum direnç özelliği göstermektedir. Çünkü Grover algoritması için çözülmesi gereken olasılık uzayı $2^{256}$ büyüklüğündedir (512-bitlik hash çıktısının karekökü). Ayrıca, yapı RSA veya ECC gibi asal çarpanlara ayırma ya da diskrét logaritma problemine dayanmadığı için Shor algoritması tarafından da doğrudan hedef alınamaz.

---

## Özellikler

* **Deterministik:** Aynı girdi için her zaman aynı hash çıktısını verir.
* **Kuantum Analojili:** Kod içerisindeki mantık, kuantum süperpozisyon ve dolanıklık analojileri ile tasarlanmıştır (matematiksel olarak kuantum değildir, sadece analojidir).
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

* `generate_super_hybrid_Kuantum_hash_v2(input_text: str) -> str`
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


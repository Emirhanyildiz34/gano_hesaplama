import ogrenci_ortalama_hesaplama as ooh

print("Genel Not Ortalaması Hesaplama\n")

ders_sayisi = int(input("Kaç dersten not gireceksiniz? "))

toplam_kredi = 0
toplam_agirlikli_puan = 0
gecen_ders_sayisi = 0

for i in range(1, ders_sayisi + 1):
    kredi, puan, gecti = ooh.ders_isle(i)
    toplam_kredi += kredi
    toplam_agirlikli_puan += kredi * puan
    if gecti:
        gecen_ders_sayisi += 1

# --- güvenlik kontrolü ---
if toplam_kredi == 0:
    print("\nHATA: Hiç geçerli kredi girilmedi. Ortalama hesaplanamaz!")
else:
    genel_ort = toplam_agirlikli_puan / toplam_kredi
    print(f"\nGENEL NOT ORTALAMANIZ (GANO): {genel_ort:.2f}")
    print(f"{gecen_ders_sayisi} dersten doğrudan geçtiniz.")

# --- Windows'ta konsolun kapanmaması için ---
input("\nÇıkmak için Enter tuşuna basın...")

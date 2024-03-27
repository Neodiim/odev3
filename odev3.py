class Personel:
    def __init__(self, adı, departmanı, çalışma_yılı, maaşı):
        self.adı = adı
        self.departmanı = departmanı
        self.çalışma_yılı = çalışma_yılı
        self.maaşı = maaşı

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print("Adı:", personel.adı)
            print("Departmanı:", personel.departmanı)
            print("Çalışma Yılı:", personel.çalışma_yılı)
            print("Maaşı:", personel.maaşı)
            print()

    def maaş_zammı(self, personel, zam_oranı):
        for p in self.personel_listesi:
            if p.adı == personel.adı:
                p.maaşı += p.maaşı * (zam_oranı / 100)

    def personel_çıkart(self, personel):
        for p in self.personel_listesi:
            if p.adı == personel.adı:
                self.personel_listesi.remove(p)
                break  

def main():
    firma = Firma()

    while True:
        print("\nYapmak istediğiniz işlemi seçin:")
        print("1. Personel ekle")
        print("2. Personel listele")
        print("3. Maaş zammı yap")
        print("4. Personel çıkart")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4/5): ")

        if secim == "1":
            adı = input("Personelin adını girin: ")
            departmanı = input("Personelin departmanını girin: ")
            çalışma_yılı = int(input("Personelin çalışma yılını girin: "))
            maaşı = float(input("Personelin maaşını girin: "))
            personel = Personel(adı, departmanı, çalışma_yılı, maaşı)
            firma.personel_ekle(personel)
            print("Personel başarıyla eklendi.")

        elif secim == "2":
            print("\nFirma Çalışanları:")
            firma.personel_listele()

        elif secim == "3":
            adı = input("Maaşını artırmak istediğiniz personelin adını girin: ")
            zam_oranı = float(input("Zam oranını girin (%): "))
            firma.maaş_zammı(Personel(adı, "", 0, 0), zam_oranı)
            print("Maaş başarıyla güncellendi.")

        elif secim == "4":
            adı = input("Çıkartmak istediğiniz personelin adını girin: ")
            firma.personel_çıkart(Personel(adı, "", 0, 0))
            print("Personel başarıyla çıkartıldı.")

        elif secim == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

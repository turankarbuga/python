
import time
import random

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal


    def ac_kapa(self):


        if(self.tv_durum=="Kapalı"):

            self.tv_durum= "Açık"
            print("televizyon açılıyor...")
            time.sleep(1)
            print("Televizyon {}".format(self.tv_durum))

        elif(self.tv_durum=="Açık"):

            self.tv_durum="Kapalı"
            print("Televizyon kapatılıyor...")
            time.sleep(1)
            print("Televizyon {}".format(self.tv_durum))

    def ses_ayar(self):
        while True:
            cevap=input("Sesi artırmak için '+' azaltmak için '-' çıkmak için 'x' ")


            if(cevap=='+'):

                if(self.tv_ses !=32):
                    self.tv_ses+=1
                    print("ses:",self.tv_ses)
                else:
                    print("ses düzeyi zaten 32")


            elif(cevap=='-'):
                if(self.tv_ses != 0):
                    self.tv_ses-=1
                    print("ses:", self.tv_ses)
                else:
                    print("ses düzeyi zaten 0")

            elif(cevap=='x'):
                break

            else:
                print("Geçersiz işlem.")

    def kanal_ekle(self,yeni_kanal):
        print("Kanal Eklendi ", yeni_kanal)
        self.kanal_listesi.append(yeni_kanal)


    def __str__(self):
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele= random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal {}".format(self.kanal))


kumanda=Kumanda()

print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç/Kapat

2. Televizyon Bilgileri

3. Kanal Sayısını Öğrenme

4. Kanal Ekle

5. Rastgele Kanal'a Geç

6. Sesi Azalt Ya da Artır
Çıkmak için 'x'
*******************""")

while True:
    islem= input("İşlem:")

    if(islem=='x'):
        print("çıkış yapılıyor...")
        time.sleep(1)
        break
    elif(islem=='1'):
        kumanda.ac_kapa()
    elif(islem=='2'):
        print(kumanda)

    elif(islem=='3'):
        print("Kanal Sayısı:",len(kumanda))

    elif(islem=='4'):

        kanallar = input("Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")

    elif(islem=='5'):
        kumanda.rastgele_kanal()
    elif(islem=='6'):
        kumanda.ses_ayar()
    else:
        print("Geçersiz işlem.")






































import random

print("Taş Kağıt Makas Oyununa Hoş Geldiniz! Oyuncu ve bilgisayar bir seçim yapar.")
print("Makas kağıdı keser, kağıt taşı sarar, taş ise makası kırar. İki tur kazanan oyunun galibi olur.")
print("Çıkmak için 'q', oyun sonunda tekrar oynamak isterseniz 'evet' yazabilirsiniz. İyi eğlenceler!\n")

secenekler = ["taş", "kağıt", "makas"]
oyuncu_skoru = 0
bilgisayar_skoru = 0

while True:
    oyuncu_tur_skoru = 0
    bilgisayar_tur_skoru = 0

    while oyuncu_tur_skoru < 2 and bilgisayar_tur_skoru < 2:
        secim = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q' tuşuna basın): ").lower()
        if secim == 'q':
            print("Oyun sona erdi.")
            break

        if secim not in secenekler:
            print("Geçersiz. Lütfen tekrar deneyin.")
            continue

        bilgisayar_secimi = random.choice(secenekler)
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

        if secim == bilgisayar_secimi:
            print("Beraberlik!\n")
        elif (secim == "taş" and bilgisayar_secimi == "makas") or \
                (secim == "kağıt" and bilgisayar_secimi == "taş") or \
                (secim == "makas" and bilgisayar_secimi == "kağıt"):
            print("Bu turu kazandınız!\n")
            oyuncu_tur_skoru += 1
        else:
            print("Bu turu kazanamadınız.\n")
            bilgisayar_tur_skoru += 1

    if oyuncu_tur_skoru == 2:
        print("Tebrikler, oyunu kazandınız!")
        oyuncu_skoru += 1
    else:
        print("Kaybettiniz. Bilgisayar oyunu kazandı.")
        bilgisayar_skoru += 1

    print(f"Genel Skor - Oyuncu: {oyuncu_skoru}, Bilgisayar: {bilgisayar_skoru}\n")

    devam = input("Tekrar oynamak ister misiniz? (evet/q): ").lower()

    bilgisayar_devam = random.choice(['evet', 'hayır'])

    if devam != 'evet' or bilgisayar_devam == 'hayır':
        print("Oyun bitti. Oynadığınız için teşekkürler!")
        break
    else:
        print("Yeni bir oyuna başlıyoruz!\n")

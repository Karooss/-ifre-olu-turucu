import random

harfler = "qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
sayılar = "1234567890"
işaretler = "+-/*!&$#?=@"
uzunluk = int(input("Parolanızın uzunluğunu giriniz:"))
sonuc = ""

for i in range(uzunluk):
    if i % 4 == 0:
        sonuc += random.choice(harfler)
    elif i % 4 == 1:
        sonuc += random.choice(sayılar)
    elif i % 4 == 2:
        sonuc += random.choice(işaretler)

print(sonuc)

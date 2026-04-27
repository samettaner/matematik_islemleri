notlar = []

sınav_sayısı= int(input("kac sınavın var: "))

for i in range(sınav_sayısı):
    deger = int(input(f"{i+1}.sınav notu: "))
    notlar.append(deger)

ortalama = sum(notlar)/len(notlar)

print("notlar: ",notlar)
print("ortalama: ",ortalama)

if ortalama >= 50:
    print("dersi gecti")

else:
    print("kaldın :) ")

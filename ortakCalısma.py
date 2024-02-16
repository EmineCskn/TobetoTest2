#1.Kullanıcının girdiği 5 basamaklı bir sayının basamaklarının toplamıyıno yazan bir döngü yazınız.
sayi=int(input("Lütfen 5 basamaklı bir sayı giriniz."))
toplam=042

while sayi !=0:
    toplam =(sayi%10) +toplam
    sayi=sayi// 10
print(toplam)

#2.Klavyeden kullanıcının girdiği 3 adet integer türünde ki 
#sayıyı büyükten küçüğe sıralayarak ortadaki sayı ile olan sayının arasındaki farkı ve yine 
#ortadaki sayı ile küçük olan sayı ile arasındaki farkı ekrana yazdıran python kodlarını yazınız?
listBox=[]
for i in range(3):
    sayi=int(input(f"Lütfen {i+1}. sayıyı giriniz.  "))
    listBox.append(sayi)
    listBox.sort
print(f"max sayi ile ortadaki sayı arasındaki fark {max(listBox)-listBox[1]}" )
print(f"min sayi ile ortadaki sayı arasındaki fark {listBox[1]-min(listBox)}" )

#3.Kullanıcının girdiği iki birbirine eşit ise ekrana “5” sonucu yazdıracak, eşit değil ise 25 defa 
#“eşit değil” sonucunu ekrana yazdıran python kodlarını yazınız? (while döngüsü ile yapılacaktır)

# sayiBir=int(input("Lütfen 1. sayıyı giriniz"))
sayiIki=int(input("Lütfen 2. sayıyı giriniz"))
i=1
if sayiBir == sayiIki:
    print(5)
else:
    while (i<26):
        print('eşit değildir\n'*25)
#5.Rastgele 600 adet 0 ile 1000 arasında sayı oluşturup bir liste içerisine aktaran ve
# 100'den küçük olan sayıların adedini ekrana yazdıran python kodlarını yazınız.
import random
list=[]
count=0
for  i in range(600):
    a=random.randint(0,1000)  #randint ramdom class'ının içinde bir method ve random int sayı üretmek için kullanıyoruz.
    list.append(a)
print(list)

for i in range(len(list)):
    if list[i] <100:
        count+=1
print(count)

#6.Kullanıcının satın aldığı
#benzinin kaç TL tuttuğunu ve bunun ne kadarının vergi
#olduğunu hesaplayıp ekrana yazdıran programı python kodları ile yazınız.
#(kullanıcı satın aldığı benzini litre cinsinden girecek - 
#Benzin litre fiyatı: 5,37 TL  - Vergi oranı %66)

kacLtre = float(input("Kaç litre benzin aldın: "))
litreFyti=5.37
toplamTutar = litreFyti*kacLtre
print(toplamTutar)
vergi=toplamTutar*0.66
print(f'vergi {vergi}')

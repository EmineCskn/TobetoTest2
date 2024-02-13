sayılar = [100, 105,305 , "merhaba", 15.5, True]
print(sayılar[1])

print(sayılar)

sayılar.append(400) #append listenin sonuna eleman ekler 

print(sayılar)

sayılar.remove("merhaba") #değere göre silme yapar
print(sayılar)

sayılar.pop(2) # index verirsek indexe göre siler vermezsek son elemanı siler 
print(sayılar)

add= [700, 800, 900]
sayılar.extend(add) # verdiğimiz elementleri listenin sonuna ekler 

print(sayılar)

sayılar.clear()
print(sayılar)

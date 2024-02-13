print("Merhaba Tobeto Test Ekibi")
#Değişkenler
#Metinsel , nümerik, objeler

text = "Merhaba"
print(text)

text1 = "selam"
print(text1)

kullaniciadi = "Emine"
print(text1+kullaniciadi)
studentcount = "45" #String
studentCount1 = 5 #integer
print(studentcount+"5")

studentcount= 5
print(studentcount+5)

averagePoint = 25.5 #double . decimal, float ondalıklı sayılar 
print(studentcount+averagePoint)

isVeriFied = True #boolean

print(isVeriFied)

print(type(text))
print(type(studentcount))
print(type(averagePoint))
print(type(isVeriFied))

#Matematiksel operatörler
number = 10
print(10+10)
print(number+number)

print(number-5)
print(number/2)
print(number*3)
print(number % 3) # sol taraftaki değerin sağ teraftaki değere bölümünden kalan 

#Mantıksal Operatörler

print(number== 10)

print(number==11) # false

print(number!= 11) #true

print(number>10) #false

print(number>= 10) #true

print(text+ " "+ kullaniciadi)

totalText = text+ " "+ kullaniciadi 
print(totalText)

totalText = "{message} Sayın {name}".format(message=text,name=kullaniciadi)

print(totalText)

#f String , format 
totalText= f"Hosgeldiniz {kullaniciadi}"
print(totalText)

print(type(totalText))
#1.
while True:
    
   kullanıcı_adi=input('isiminiz')
   kullanici_sifre=input('şifreniz')

   if kullanıcı_adi=='mehmet' and kullanici_sifre=='123':
    print('giriş başarılı')
    break
   else:
    print('giriş başarısız tekrar deneyiniz')
    continue

print('\n')

#2.

isim=input('isim')
soyisim=input('soyisim')
yas=input('yasınız')

print('hosgeldin' " " + isim +" "+ soyisim+" "+'yaşınız'+" "+ yas)

print("\n")

#3.

market_listesi=['elma','cips','yoğurt','armut']
market_listesi.append('kalem')
print("market listesindekiler \n") 
print(market_listesi)

#4.

dictionary={
"klavye":500,
"mouse":200,
"kalem":20,
"kitap":150,
"bardak":70,
"telefon":2000,
  }
  

print('ürünler')
print(':')


for d in dictionary:
   print(d)

#5.
while True:
  
 ürün = input("fiyatları görmek için bir Ürün giriniz ")

 if ürün in dictionary:
    print(ürün, "fiyat:", dictionary[ürün], "TL")
    break
 else:
    print("Ürün bulunamadı\n")
    continue
print('\n')

#BURADAN GERİSİNİ YAPAMADIM

#6.

print('PAZAR GÜNÜ ALINACAKLAR')

yeni_tuple=('masa','defter','saz','çukulata','kutu','klavye','saat','koltuk')
print(yeni_tuple)
print('\n')


print('PAZAR GÜNÜ ALINMAMIŞLAR VE ALINMASI GEREKENLER')

yeni_tuple_2=('kalem','masa','koltuk','saz','klavye','makas','şişe')
print(yeni_tuple_2)
 
print('\n')


alacaklar=set(['patlıcan','tava','tereyağı','bez'])

alacaklar.discard('armut')

if alacaklar:

   print(alacaklar)




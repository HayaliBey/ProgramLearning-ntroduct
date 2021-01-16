#Fonksiyonlar
#print("İlk Sayfa")
#krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"] #Böyle veriler genellikle bir veri kaynağından gelir. Alttaki işlemler ise bu veri alındıktan sonra yapılacak olan işlemlerdir.

#alias
#for turler in krediler: #for in döngüsü, türleri yazdırdım. Buna alias yani takma ad diyoruz.
  #print("<option>"+turler+"<option>") #option'lar içindeki türü bir sitede açılır kutuda bir eleman gibi göstermek için kullanılır. Şu ân bir önemi yok.

#print(" ")

#print("İkinci Sayfa")
#krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"] #Böyle veriler genellikle bir veri kaynağından gelir. Alttaki işlemler ise bu veri alındıktan sonra yapılacak olan işlemlerdir.

#alias
#for turler in krediler: #for in döngüsü, türleri yazdırdım. Buna alias yani takma ad diyoruz.
  #print("<option>"+turler+"<option>") #option'lar içindeki türü bir sitede açılır kutuda bir eleman gibi göstermek için kullanılır. Şu ân bir önemi yok.

#print(" ")

#print("Üçüncü Sayfa")
#krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"] #Böyle veriler genellikle bir veri kaynağından gelir. Alttaki işlemler ise bu veri alındıktan sonra yapılacak olan işlemlerdir.

#alias
#for turler in krediler: #for in döngüsü, türleri yazdırdım. Buna alias yani takma ad diyoruz.
  #print("<option>"+turler+"<option>") #option'lar içindeki türü bir sitede açılır kutuda bir eleman gibi göstermek için kullanılır. Şu ân bir önemi yok.

#print(" ")

#Örneğin kredilerden biri iptal olsa, meselâ Hızlı Kredi kısmı kaldırılsa. Ki böyle birşey şu ân kolay, çünkü 3 sayfa verisi var, yâni düzelmesi kolay. Ama gerçek hayatta milyonlarca satır kod olduğu için teker teker uğraşamayacağımız için Yukarıdaki kodu tamamen algılanmaz hâle getirip kısaca çözüme gidiyorum:

#Şu ân yapacağım şey bir tanım. Yani :'dan sonra yazdıklarım, kredileriListele'nin içinde olacak ve ben kredileriListele yazınca içindeki neyse o çalışacak. Tanımlama yaptığım için de çalıştırdığımda ekranda birşey yazmayacak bir kod yazıyorum:
def kredileriListele(): #defination fonksiyonu, parantez açıp kapatmak bize bir fonsiyon olduğunu hatırlatır. kredileriListele deme sebebimiz alttaki kod bloğuna verdiğimiz hatırlatıcı isim.
  krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"]
#Böyle veriler genellikle bir veri kaynağından gelir. Alttaki işlemler ise bu veri alındıktan sonra yapılacak olan işlemlerdir.

#alias
  for turler in krediler: #for in döngüsü, türleri yazdırdım. Buna alias yani takma ad diyoruz.
    print("<option>"+turler+"<option>") #option'lar içindeki türü bir sitede açılır kutuda bir eleman gibi göstermek için kullanılır. Şu ân bir önemi yok.


kredileriListele() #Şu ân fonksiyonu çağırdım ve çalıştırdığımda
#<option>Hızlı Kredi<option>
#<option>Maaşını Halkbank'tan alanlara özel<option>
#<option>Mutlu Emekli İhtiyaç Kredisi<option>
#yazdı.



#Diyelim ki 'Hızlı Kredi' iptal oldu. Yâni şu kısım krediler = ["Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"] böyle kaldı. Önceki gibi bir hata olmaz ve fonksiyon çalışır. Ve:
#<option>Maaşını Halkbank'tan alanlara özel<option>
#<option>Mutlu Emekli İhtiyaç Kredisi<option>
#Ekranda böyle çıktı verir. Böylece tek bir yeri değitirerek sorunu çözmüş oluruz.

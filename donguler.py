#Döngüler
krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"] #Böyle veriler genellikle bir veri kaynağından gelir. Alttaki işlemler ise bu veri alındıktan sonra yapılacak olan işlemlerdir.

#alias
for turler in krediler: #for in döngüsü, türleri yazdırdım. Buna alias yani takma ad diyoruz.
  print("<option>"+turler+"<option>") #option'lar içindeki türü bir sitede açılır kutuda bir eleman gibi göstermek için kullanılır. Şu ân bir önemi yok.

print(" ")

for i in range(10): #range 10 kere çalışacak. i'ye 0'dan 9'a kadar değer verecek.
    print(i) #i'yi yazdır dediğim için alt alta 0'dan 9'a yazdıracak. 10 yerine len(krediler) yazarsak 3 defa çalışacak. i'ye 0'dan 2'ye kadar değer verecek. 0'dan 2'ye yazdırabileceğiz.

print(" ")

for turler in range(len(krediler)):
  print(turler)

print(" ")

for i in range(len(krediler)):
  print(krediler[i]) #krediler dizisinin boyu 3 (0,1,2) olduğu için i=0'da dizinin ilk elemanı olan 'Hızlı Kredi'yi yazdıracak ve bi alt satıra geçecek. i=1'e bakacak ve dizinin ikinci elemanı olan 'Maaşını Halkbank'tan alanlara özel' yazacak ve bir alt satıra geçip aynı işlemleri uygulayacak. Böylece dizideki 3 eleman alt alta yazdırılmış olacak.

print(" ")

for i in range(4,10): #Matematik'teki açık paranteze benzer şekilde (4,10] burda da açık parantez kullanıldığında, ilk sınırdaki yâni gördüğümüz sayılardan sol taraftaki ve aradaki sayıların dâhil olduğunu fakat sağdaki sayının dâhil olmadığını anlayacağız.
    print(i)

print(" ")

for i in range(0,11,2): #0'dan başla 10'a kadar (10 dâhil değil) 2'şer 2'şer say, alt alta yaz.
  print(i)


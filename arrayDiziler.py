#Örneğin bir e-ticaret uygulamasında bir arama yaptığımızda gösterilen ürünlerin her biri array'de tanımlı 
krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"]
print(krediler)
print(krediler[0]) #ilk eleman 0. eleman. Çünkü her dizide ilk eleman 0'dır.
print(krediler[1]) #ikinci eleman
print(krediler[2]) #üçüncü eleman

print(len(krediler)) #length (uzunluk) yani dizide kaç karakter varsa onu gösteriyor.

krediler[0] = "Cabuk kredi" #ilk elemanın adını değiştirdik
print(krediler) #değişen ilk elemanı ekranda görmek için yazdırdık.

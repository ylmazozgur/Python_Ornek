# Verilen basamak sayısına kadar olan tüm palindrom sayılarını ve verilen basamak sayısındaki(basamak değeri 3 -> 100 - 999) palindrom sayılarını yazdıralım.

def Counter_Of_Palindrom(digits):
    digits = 10**digits # basamaklarla uğraştığım için üstel bir fonksiyon yazdım.
    counter = 0 # Toplam palindrom sayısını bulmak için bir tane sayaç değişkeni ekledim.
    liste = [] # Palindrom olan sayıları görmek için liste oluşturdum. #İsteğe bağlı, istersem eklememe gerek yoktu.
    for i in range(1,digits): # Döngümüz 1'den digits(basamak değeri)'e kadar ilerleyecek.
        if str(i) == str(i)[::-1]: # Palindrom olup olmadığını kontrol ettiğimiz nokta.
            counter += 1 # Palindrom ise sayacı 1 arttırdım.
            liste.append(i) # Palindrom ise o sayıyı listenin sonuna ekledim.
    print(liste) 
    #print(f" sayaç:{counter}, uzunluk:{liste[-1]}")
    a = sayac(digits)
    return [a, counter]

# Yukarıdaki for döngüsünü "list comprehension" olarak yazmak istersek, alttaki gibi yazabiliriz. 
# counter = sum(1 for i in range(10000,100000) if str(i) == str(i)[::-1])
# print(counter)

def sayac(digits): # 1 basamaklı sayıları dahil etmemek için yazdığım kod.
    sonuc = sum(1 for i in range((digits // 10 ), digits) if str(i) == str(i)[::-1]) 
    return sonuc


Counter_Of_Palindrom(100)

""" Yukarıdaki kodu yazabiliriz. Teoriksel olarak yazdığımızda istenilen sonucu verecektir. Yalnız yukarıdaki kodu çalıştırırsak çok uzun süreceği için "Execution Timed Out" hatası almamız muhtemeldir. Bu yüzden daha efektif ve verimli olması için matematiksel formülünü kullanarak yazacağız.
"""

def Sayac(n):
    Toplam_Sayac = 0
    for i in range(1, n + 1):
        Sayac = 9 if i == 1 else 9 * 10 ** ((i - 1) // 2)
        Toplam_Sayac += Sayac
        print(f"{i}-basamaklı palindrom sayılarının sayısı: {Sayac}")
    print(f"10^{n} sayısının altındaki toplam palindrom sayıların sayısı: {Toplam_Sayac}")
    return [Sayac, Toplam_Sayac]

Sayac(5)

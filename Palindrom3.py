# Türkçe

# "elements" dizisi ve "n" bir tamsayı olarak alınmıştır. Görevimiz, bu dizi içerisinden alınan elemanlarla uzunluğu "n" olan bir palindrom dizisi oluşturmaktır.

# ŞARTLAR

# 1) Palindrom verilen dizinin ilk elemanıyla başlayacaktır.
# 2) Bir çift elde edildikten sonra, diğer elemanı palindroma ekleyeceğiz. Ör: [11] olduysa [112] olacak.
# 3) Elde edilen çiftten sonra gelecek olan eleman, o çiftin arasına yerleşecek. Ör: [11] olduysa [121] olacak.
# 4) Eğer verilen dizinin son elemanına ulaşılırsa, süreç en baştan devam ettirelecektir.
# 5) Hata durumunda:
# 5.1) dizi boş veya n < 2 olduğu durumlarda "Error" ifadesi dönecektir.

#----------------------------------------------------

# English

# You are given string "elements" and an int "n". Your task is to return a string that is a palindrom using elements from the string "elements" with the length "n".

# The format of the palindromization:

# Your palindrome begins with the first element of "elements".
# After obtaining a pair, you insert the next element in "elements" to the palindrome.
# The next element will be paired inside the first pair.
# Repeat
# If you have reached the last element of "elements" then repeat the process from the start.
# Error cases:
# If the string elements is empty or n is smaller than 2, return the string "Error!"

#----------------------------------------------------




#Öncelikle bu soruyu iki aşamalı düşüneceğiz.
# Birinci aşama, Palindromlar baştan sona ve sondan başa aynı olan şeyler olduğunu biliyoruz. "123321" bu örneğe baktığımızda, "123" ve "321" bize, bu soruyu çözmek için 'ilk yarısını al, sonra ikinci yarısını yazdır' ipucusunu anlamamız gerekiyor.
# Peki ya bu ilk yarısını nasıl yazdıracağız? -> İlk önemli kısım.
# Peki ya bu ikinci yarısını nasıl yazdıracağız? -> İkinci önemli kısım. 
# Adım adım ilerleyeceğiz.

elements = "123" 
yarisi = [] # İlk yarısını yazdıracağımız liste
for i in range(3 // 2): # Listenin yarısını yazdırmak için " // 2" yazıyoruz.
    print(f"{i+1}. döngü") # Döngüyü görmek adına çıktı aldım.
    index = i % len(elements) # index değeri bizim için ilk yarısını yazdırmaya yarıyacaktır. Buradaki "i % len(elements)" matematikteki mod alma işlemidir. Biz "elements" içindeki değerleriyle bir Palindrom yazdırmak istiyoruz!! Bu yüzden bir index sayısına ihtiyacımız var.
    yarisi.append(elements[index]) # Almış olduğumuz index sayısı ile ilk yarısını yazdıracağımız listeye, elements içindeki değerleri yazdırıyoruz. Ör: "123231123" gibi... Bu değerler dışında başka bir değer olmaması için index aldık.
    print(yarisi)

ikinci_yarisi = yarisi.copy() #ilk yarısı olan palindromun kopyasını başka bir değişkene kopyaladık. Eşitlemedik!!! Kopyaladık!!!
if 3 % 2 != 0: #Çift sayılarda bir orta değer bulunmadığı için bir şey yapmamıza gerek yok. Ama bu tek olan sayılar için geçerli değil.
    Orta_Index = 3 // 2 % len(elements) #orta indeks değerini buluyoruz.
    ikinci_yarisi.append(elements[Orta_Index])
    print(ikinci_yarisi)
ikinci_yarisi.extend(yarisi[::-1]) #Son oluşturmuş olduğumuz listeye, ilk yarısı listesinin tersini yazdırıyoruz.
"".join(ikinci_yarisi)


# Burada yukarıda yazmış olduğum kodu fonksiyona dönüştürdüm.
def pal(elements, n):
    if not elements or n < 2:
        return "Error"
    yarisi = []
    for i in range(n // 2):
        index = i % len(elements)
        yarisi.append(elements[index])

    ikinci_yarisi = yarisi.copy()
    if n % 2 != 0:
        Orta_Index = n // 2 % len(elements)
        ikinci_yarisi.append(elements[Orta_Index])
    ikinci_yarisi.extend(yarisi[::-1])
    return "".join(ikinci_yarisi)

pal("123",3)


# Farklı bir yazım için buna da bakabiliriz.

# def palindromization3(elements, n):
#     if not elements or n < 2:
#         return "Error!"
#     half = [elements[i % len(elements)] for i in range(n // 2)]
#     result = half + ([elements[n // 2 % len(elements)]] if n % 2!= 0 else []) + half[::-1]
#     return "".join(result)


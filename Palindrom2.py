#Türkçe
# Bize bir dizi veriliyor. Bu dizi palindromik ve palindromik olmayan sayılardan oluşuyor. Görevimiz ise, palindromik olan elemanları ve olmayan elemanları bul. Sonra bir diziye, palindronik olar eleman için 1, palindromik olmayan eleman için 0 yazsın.

#-------------------------------------------
#English

# An array is given with palindromic and non-palindromic numbers. A palindromic number is a number that is the same from a reversed order. For example 122 is not a palindromic number, but 202 is one.

# Your task is to write a function that returns an array with only 1s and 0s, where all palindromic numbers are replaced with a 1 and all non-palindromic numbers are replaced with a 0.

# For example:

# [101, 2, 85, 33, 14014]  ==>  [1, 1, 0, 1, 0]
# [45, 21, 303, 56]        ==>  [0, 0, 1, 0]

#-------------------------------------------

a = [101,2,85,33,14014] 

def ispalindrom(palindrome):
    liste = []
    for i in palindrome:
        if str(i) == str(i)[::-1]:
            liste.append(1)
        else:
            liste.append(0)
    return liste

ispalindrom(a)

#Yukarıdaki kod çalışır. Başka nasıl yazılır diye merak edersek;

def palindrom2(sayi):
    return [str(n)==str(n)[::-1] for n in sayi]
palindrom2(a)


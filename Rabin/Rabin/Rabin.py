#Рабин 
import random
import math
import re
from Crypto.Util import number


def primes(num):
    if 2 <= num:
        yield 2
    for i in range(3, num + 1, 2):
        if all(i % x != 0 for x in range(3, int(math.sqrt(i) + 1))):
            yield i

#На больших числа тупит
def big_mod_prime(before,size):#Бефор-до какого числа генерируется значения(правая граница).Сайз-левая граница
    z = list(primes(before))
    print(z)
    z = [x for x in z if x  > size]#Оставляет ток элементы выше  size
    z = [x for x in z if  (x % 4) == 3]#Оставляет только те что z mod 4 = 3
    position = random.randint(0, len(z) -1)
    return z[position]


#Огонь и пушка
def fast_big_mod_prime(len):
    primeNum = 0
    while  (primeNum % 4 != 3):
        primeNum = number.getPrime(len)
    return  primeNum


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def ASCIItoText(number):
    number = str(number)
    size = len(number)
    if (size % 2 != 0 ):
        number = "0" + number
    number = [number[i:i+2] for i in range(0, len(number),2)]
   # number =   (str(([  chr( int(number[i]) ) for i in range( 0, len( number ) )])))
    number =  (([  chr( int(number[i]) ) for i in range( 0, len( number ) )]))
    return (''.join(number))


def ev(a,b):
    c = 1
    for k in range(abs(a)):
        if ( c - b * k ) % a == 0:
            y = k
            x = ( c - b * y ) // a
            return x,y
  
#    Сделать оч большим
#Right = 300
#Left = 15
#q = big_mod_prime(Right,Left)
#p = big_mod_prime(Right,Left)


#размер NORM OT 100 DO 1000
size_bit = 50
q = fast_big_mod_prime(size_bit )
p = fast_big_mod_prime(size_bit)


print("Закрытые случайные ключи")
print(f"q = {q}")
print(f"p = {p}")

n = q*p
print("Открытый ключ n -", n)

#Создаем сообщение М<n
#M = int(input('Введите M:'))
M_i= str(input('Введите сообщение:'))
print("\nИсходное сообщение:", M_i)
M_i =[ord(c) for c in M_i]
#print("Исходное сообщение:", M_i)
M =" "
for i in M_i:
    M += str(i)
M = int(M)
print("Исходное сообщение :", M)

#Шифрование
C = pow(M, 2, n)
print('\nЗашифрованное сообщение:', C)
 
#Расшифровка
m1 = pow(C, (p+1)//4, p)# c^((p+1)/4) mod p

m2 = -pow(C, (p+1)//4, p)
#m2 = (p - C**((p+1)//4)) % p
m3 = pow(C, ((q+1)//4), q)
#m4 = (q - C**((q+1)//4)) % q
m4 = -pow(C, (q+1)//4, q)

#вычислим a и b
a = q * pow(q, p-2, p) 
b = p * pow(p, q-2, q)

#a = int(q * ((q**(-1)) % p))
#b = int(p *((p**(-1))% q))

print("tocka 2")

#получаем 4 текста  
M1 = (a * m1 + b * m3) % n
M2 = (a * m1 + b * m4) % n
M3 = (a * m2 + b * m3) % n
M4 = (a * m2 + b * m4) % n

print("Расшифровки")
print("Вариат 1=",M1)
print("Вариат 2=",M2)
print("Вариат 3=",M3)
print("Вариат 4=",M4)

print(f"\nВариат 1 =   {ASCIItoText(M1)} \n")
print(f"Вариат 2 =   {ASCIItoText(M2)} \n")
print(f"Вариат 3 =   {ASCIItoText(M3)} \n")
print(f"Вариат 4 =   {ASCIItoText(M4)} \n")



#Через линейное диофантово уравнение (оч медленно)
#yp,yq = ev(p,q)
#r1 = (yp*p*m3 + yq * q * m1) % n
#r2 = n - r1
#r3 =(yp*p*m3 - yq * q * m1) % n
#r4 = n - r2
#
#print("Расшифровки")
#print("Вариат 1=",r1)
#print("Вариат 2=",r2)
#print("Вариат 3=",r3)
#print("Вариат 4=",r4)
#
#print(f"\nВариат 1 =   {ASCIItoText(r1)} \n")
#print(f"Вариат 2 =   {ASCIItoText(r2)} \n")
#print(f"Вариат 3 =   {ASCIItoText(r3)} \n")
#print(f"Вариат 4 =   {ASCIItoText(r4)} \n")

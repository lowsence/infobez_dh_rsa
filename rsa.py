import random
from math import gcd

#проверка на взаимно простые числа
def co_prime(a, b):
    return gcd(a, b) == 1


def prime_number():
    n = int(input("ENTER THE AMOUNT OF NUMBERS IN THE ARRAY: "))
    array = []
    # заполнение массива числами от 0 до n
    for i in range(n + 1):
        array.append(i)
    print("\n ORIGINAL ARRAY: \n", array, "\n\n")
    # число 1 не является простым
    array[1] = 0
    #проверка всех чисел на простоту
    i = 2
    while i ** 2 <= n:
        if array[i] != 0:
            j = i * 2
            while j <= n:
                array[j] = 0
                j += i
        i += 1
    #удаление повторяющихся чисел и вывод массива с простыми числами
    array = set(array)
    array.remove(0)
    print("\n MODIFIED ARRAY OF PRIME NUMBERS: \n", array, "\n\n")

    array = list(array)
    #простое число P
    index = random.randint(0, len(array) - 1)
    number_1 = array[index]
    array.remove(number_1)
    #простое число Q
    index = random.randint(0, len(array) - 1)
    number_2 = array[index]
    array.remove(number_2)
    #вывод массива простых чисел без чисел P и Q
    array = set(array)
    print("\n MODIFIED ARRAY OF PRIME NUMBERS WITHOUT P AND Q: \n", array)

    return array, number_1, number_2


rsa_array, p, q = prime_number()
rsa_array = list(rsa_array)
print("\n", "PRIME NUMBER 1: P =", p, "\n", "PRIME NUMBER 2: Q =", q)

n = p * q
f = (p - 1) * (q - 1)
print("\n", "MODULE N =", n, "\n", "(P - 1) * (Q - 1) =", f)

e = random.choice(rsa_array)
print(" PRIME SECRET NUMBER E=", e)
#
if not (1 < e < f) or not co_prime(e, f):
    print("CHANGE PRIME NUMBER")
    rsa_array.remove(e)
    e = random.choice(rsa_array)
    print("CHANGE PRIME NUMBER =", e)

for d in range(3, f, 2):
    if d * e % f == 1:
        break

print(" SECRET NUMBER D =", d)

m = int(input("\nENTER THE NUMBER: "))
#шифрация числа
encrypt = (m ** e) % n
#дешифрация числа
decrypt = (encrypt ** d) % n

print("\nENCRYPTION =", encrypt)
print("\nDECRYPTION =", decrypt)

if decrypt == m:
    print("\nDECRYPTION COMPLETED")
else:
    print("\nDECRYPTION FAILED")
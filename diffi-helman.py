import random

#2 случайных числа G и P, известные Алисе, Бобу и злоумышленнику
g = random.randint(0, 5000)
p = random.randint(0, 5000)
print("PUBLIC: \tG =", g, "\nPUBLIC: \tP =", p, "\n")

#2 случайных числа A и B, заданные секретно Алисой и Бобом
a_num = random.randint(0, 10000)
b_num = random.randint(0, 10000)
print("SECRET: \tAlice's number =", a_num, "\nSECRET: \tBob's number =", b_num, "\n")


#расчет персональных секретных ключей для Алисы и Боба по формуле
a_pers_key = (g ** a_num) % p
b_pers_key = (g ** b_num) % p
print("SECRET: \tAlice's personal key =", a_pers_key, "\nSECRET: \tBob's personal key =", b_pers_key, "\n")

#расчет публичного ключа, одинакового для Алисы и Боба по формуле
a_final_key = b_pers_key ** a_num % p
b_final_key = a_pers_key ** b_num % p
print("PUBLIC: \tAlice's final key =", a_final_key, "\nPUBLIC: \tBob's final key =", b_final_key)

#Вывод
if (a_final_key == b_final_key):
    print("\t\n\t        SUCCESSFULLY COMPLETED\n")
else:
    print("\t\n\t        FAILED\n")

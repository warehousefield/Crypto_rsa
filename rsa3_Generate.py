from rsa2 import d, e, n, fn, p, q

# GENERATION AND CHECK: 

print("d=", d, "e=", e, "n=", n, "fn=", fn,"p=", p, "q=", q, end=" ")

# Проверка совместимости ключей:
if e < fn:
    check_e = True
else:
    check_e = False
#print(check_e)

# Проверка p и q:
if p != q:
    check_pq = True
else:
    check_pq = False
#print(check_e, check_pq, end="")

# Проверка fn и d:
if d < fn:
    check_d = True
else:
    check_d = False
print(check_e, check_pq, check_d, end="")
print(n.bit_length())

# Если получим True по 3м проверкам, то копируем и вставляем сгенерированные ключи e,n,d в файл rsa5_Crypto.py

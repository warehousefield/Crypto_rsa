# COPY-PAST KEYS here, for example:
# d= 1207683 e= 547 n= 1783279 
# d= 33552185627 e= 67 n= 2247999435673  

d= 33552185627 
e= 67 
n= 2247999435673 



# Сообщение m from Bob to Alice:
# ВАШЕ СООБЩЕНИЕ ПИШЕМ ТУТ, например - Apple;
m = "Apple;" # YOUR MESSAGE

# Конвертация букв в числа индекса:
mncx = list(m)
zzz = []
for i in mncx:
    xxx =ord(i)#-86 
    zzz.append(xxx)
print("Indexes=",zzz)    
# Cоздаем список mmm из подготовленных индексов исходного сообщения m
mmm = []
for j in zzz:
    #if j == -54:
        #j+= 64 
    mmm.append(j)

# Шифруем список mmm алгоритмом Rsa:
encrypt = []
for k in mmm:
    fff = pow(k, e, n)
    encrypt.append(fff)

print("encrypt RSA Bob=", encrypt)

# Расшифровка Rsa Alice:
decrypt = []
for l in encrypt:
    hhh = pow(l, d, n)
    decrypt.append(hhh)

print("decrypt RSA Alice=", decrypt)

# Обратный перевод индексов в буквы:
dec = []
for p in decrypt:
    #p+=86
    bob = chr(p)
    dec.append(bob)
    #print(ord(i), end="")
print("dec first message=",dec)

# Message:
print("YOUR FIRST MESSAGE=")
print(''.join(map(lambda x: str(x),dec)))

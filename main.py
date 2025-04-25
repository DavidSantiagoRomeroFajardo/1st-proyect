import random 
letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Que tan larga es la contraseña:"))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(letras)
print(contraseña)    
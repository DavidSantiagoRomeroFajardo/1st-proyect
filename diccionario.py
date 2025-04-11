
Palabras_modernas = {
    "LOL" : "una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL" : "una respuesta a una broma",
    "SHEESH" : "ligera desaprobación",
    "CREEPY" : "aterrador, siniestro",
    "AGGRO" : "ponerse agresivo/enojado",
    "CHEVERE" : "algo genial o increible",
    "VAINA" : "se referie a algo",
    "PARCERO" : "forma de llamar un amigo",
    "POLA" : "forma de referirse a la cerveza",
    }
word = input("Hola, escribe una palabra que no entiendas(En mayuscula)")
for i in range(5):
    if word in Palabras_modernas.keys():
        print(Palabras_modernas[word])
    else:
        print("No conozco esa palabra")

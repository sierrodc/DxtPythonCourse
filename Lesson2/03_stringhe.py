str = "hello world"


# stringa come array
print(str[0])
print(str[-1])
print(str[0:5])
print(str[6:-4])
print(str[0:-1:2])
print(str[0::2]) ######### QUESTION: per mostrare anche l'ultimo carattere, basta non mettere il limite di destra ma solo start e step


print(len(str))
# alcuni "metodi" della "classe" str
print(str.upper())
print(str.replace("o", "@"))
print(str.replace("o", "@", 1))
print(str.split(" "))


# formattazione
numero = 0.5
print("[old] Questa è %s stringa di formattazione: %d" % (int(numero*2), str.upper()))
print("[old] Questa è {} stringa di formattazione: {}".format(int(numero*2), str.upper())) # https://pyformat.info/
print(f"[new] Questa è {int(numero*2)} F-string di formattazione: {str.upper()}")
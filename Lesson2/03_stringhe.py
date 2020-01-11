str = "hello world"

# stringa come array
print(str[0])
print(str[-1])
print(str[0:5])
print(str[6:-4])
print(str[0:-1:2])

# alcuni "metodi" della "classe" str
print(len(str))
print(str.upper())
print(str.replace("o", "@"))
print(str.replace("o", "@", 1))
print(str.split(" "))

# formattazione
numero = 0.5
print("Questa è %s stringa di formattazione: %d" % (int(numero*2), str.upper()))
print("Questa è {} stringa di formattazione: {}".format(int(numero*2), str.upper())) # https://pyformat.info/
print(f"Questa è {int(numero*2)} F-string di formattazione: {str.upper()}")
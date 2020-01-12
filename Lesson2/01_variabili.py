# variabile: etichetta riutilizzabile contenente un valore salvato in memoria.

# questi sono numeri:
import sys
numero_intero = 5
numero_reale = 2.7
numero_complesso = 1+1j

# questa è una stringa di testo
stringa = "Questa è una stringa"  # lunga 20 caratteri
stringa2 = 'Anche questa è una stringa'
stringa3 = "Perchè l'interpreter accetta entrambe?"
stringa4 = 'Perchè l\'interpreter accetta entrambe?'
stringa5 = input("Scrivi qualcosa\n")

# stampo il contenuto
print(numero_intero)
print(numero_intero + numero_intero)
print(numero_reale)
print(numero_complesso)
print(numero_complesso + numero_intero)
print(stringa)

# stampo il tipo di ogni variabile
print(type(numero_intero))
print(type(numero_reale))
print(type(numero_complesso))
print(type(stringa))
# stampo la memoria occupata in bytes per ogni variabile
print(sys.getsizeof(numero_intero))
print(sys.getsizeof(numero_reale))
print(sys.getsizeof(numero_complesso))
print(sys.getsizeof(""))
print(sys.getsizeof(stringa))


# conversioni di tipo
print(int(numero_reale))
print(complex(numero_reale))
print("numero reale convertito a intero: " + str(int(numero_reale)))


numero_intero = "3.14"
print(numero_intero)
print(type(numero_intero))
print("Numero intero : " + numero_intero)
print("Numero intero : " + str(numero_intero))
print("Numero reale convertito a intero: " + int(numero_reale))
print(float(numero_intero))

# Curiosità
numero_intero_moltogrande = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
print(numero_intero_moltogrande+1)
print(type(numero_intero_moltogrande))
print(sys.getsizeof(numero_intero_moltogrande))

numero_reale_moltogrande = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.99999999999999999999999999
print(numero_reale_moltogrande+1)
print(type(numero_reale_moltogrande))
print(sys.getsizeof(numero_reale_moltogrande))

# print(sys.float_info)

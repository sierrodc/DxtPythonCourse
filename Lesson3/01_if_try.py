import sys

a = int(input("Write a number\n"))

if a > 6:
    print("a > 6")
elif a <= 0:
    print("a <= 0")
elif a <= 3:
    print("a <= 3")
else:
    if a == 4:
        print("a = 4")
    else:
        print("a = 4")

if a > 2:
    a = 1
    b = 3
elif a > 0:
    print(f"a maggiore di zero. B = {b}")

print(f"B = {b}")

try:
    value = int(input("Insert a number\n"))
    print(100/value)
except ZeroDivisionError:
    print("Division by zero")
except ValueError as e:
    print(f"Error {e.args[0]}")
except:
    ex = sys.exc_info()[1]
    print("Error")
else:
    print("Nessun errore riscontrato")
finally:
    print("Sempre eseguito (i.e.: chiudi file)")
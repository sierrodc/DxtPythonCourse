import sys

a = int(input("Write a number (try 2):\n"))

if a > 6:
    print("a > 6")
elif a <= 0:
    print("a <= 0")
elif a <= 3:
    pass
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


# -------------------- TRY -----------------

try:
    value = int(input("Insert a number\n"))
    print(100/value)
except ZeroDivisionError:
    print("Division by zero")
except ArithmeticError:
    pass
except ValueError as e:
    print(f"Error {e.args[0]}")
except Exception as e:
    print(f"Error {e}")
except:
    ex = sys.exc_info()[1]
    print("Error")
else:
    print("Nessun errore riscontrato")
finally:
    print("Sempre eseguito (i.e.: chiudi file)")


try:
    value = int(input("Insert a number\n"))
    print(100/value)
except Exception as e:
    print(f"Error {e}")
except KeyboardInterrupt:
    print("ahhahah KeyboardInterrupt")
except:
    ex = sys.exc_info()[1]
    print("Error")
else:
    print("Nessun errore riscontrato")
finally:
    print("Sempre eseguito (i.e.: chiudi file)")


# ----------------- WHEN --------------------
with open('C:/Users/rober/Desktop/test.txt') as f:
    for line in f:
        print(line)

# equivalente a 
try:
    f = open('C:/Users/rober/Desktop/test.txt')
    # ...
finally:
    f.close()
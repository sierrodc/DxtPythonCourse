import sys
#-------------------------------------------------------
#Generators: funzione che ritorna, di volta in volta, un valore

def simpleGenerator(start, stop, step):
    while(start < stop):
        yield start
        start = start + step

for i in simpleGenerator(0, 10, 2):
    print(i)


#-------------------------------------------------------
# more complex generator: sequenza di fibonacci (0,1,1,2,3,5,8...)
def generatoreFibonacci(maxValue):
    index = 0
    a, b = 0, 1
    while a < maxValue:
        yield (index, a)
        index = index + 1
        a, b = b, a + b

myGenerator = generatoreFibonacci(10000000000000000000000)
for i in myGenerator:
    print(f"{i[0]}° = {i[1]}")
    if i[1] > 100:
        break


#-------------------------------------------------------
# alcune funzioni utili: 
myGenerator = generatoreFibonacci(1000)
for i in myGenerator:
    print(f"{i[0]}° = {i[1]}")
    if i[1] > 100:
        break

print(myGenerator)
print(next(myGenerator))
print(list(myGenerator))




#-------------------------------------------------------
# short version: "generator comprehension" vs "list comprehension"
# syntas: (expression for i in iterator if i_condition)
quadratoList = [num**2 for num in range(50) if num != 10]
quadratoGnrt = (num**2 for num in range(50) if num != 10)
print(sys.getsizeof(quadratoList))
print(sys.getsizeof(quadratoGnrt))

# generatore infinito:
def generatoreFibonacciInfinito():
    index = 0
    a, b = 0, 1
    while True:
        yield (index, a)
        index = index + 1
        a, b = b, a + b

for i in generatoreFibonacciInfinito():
    print(i)



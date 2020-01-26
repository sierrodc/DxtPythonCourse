from _02_puntatore import miaFunzioneRichiedeCallback

def myFunction(a, b):
    return a + b

myLambdaFunction = lambda a,b : a+b

print(myFunction(1,2))
print(myLambdaFunction(1,2))


# -------------------------------
# come può essere realmente usato:
miaFunzioneRichiedeCallback(1,2, lambda msg: print(msg))

# oppure meglio
myList = [1,2,3,4,5]
print(myList * 2)
print(list(map(lambda x: x*2, myList)))
print(list(filter(lambda x: x % 2==0, myList)))
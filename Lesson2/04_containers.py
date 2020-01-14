# [List]: collezione ordinata e modificabile, duplicati ammessi
# (Tuple): collezione ordinata e non modificabile, duplicati ammessi
# {Set}:  collezione non ordinata e modificabile, duplicati non ammessi
# {key:val}: collezione chiave-valore, non ordinata e modificabile. duplicati non ammessi

# -------------------------------
# ------------ LIST  ------------
# -------------------------------

lista = [None] * 10 ######### QUESTION: per preallocare una lista di 10 items

lista = ["uno", "due", "tre", "quattro"]
print(type(lista))
print(lista)
print("uno" in lista)
print(lista[1])
lista[1] = "_D_U_E_"
print(lista)
lista.append("cinque")
lista.insert(0, "zero")
print(lista)
print(len(lista)) # lunghezza list
# con la lista si può implementare uno STACK (LIFO) o una QUEUE (FIFO)

# WARNING
lista[2] = 3
print(lista)

# -------------------------------
# ------------ TUPLE ------------
# -------------------------------
tupla = ("uno", "tre", "tre") # = tuple(["uno", "due", "tre"])
print(type(tupla))
tupla[1] = "due"
print(tupla)
print("uno" in tupla)

# -------------------------------
# ------------  SET  ------------
# -------------------------------
insieme = {"uno", "tre", "tre"} #= set(["uno", "due", "tre"])
insieme[1] = "ciao"
print(type(insieme))
insieme.add("quattro")
insieme.add("quattro")
print(insieme)
print("uno" in insieme)
insieme.remove("uno")
print(insieme)
insieme.discard("uno")
print(insieme)
insieme.remove("uno")
print(insieme)

# -------------------------------
# ------------ DICT  ------------
# -------------------------------

dic = {
    'IsTest': True,
    'DatabaseConnection': "DatabseConnection=",
    'DbName': "DWHP",
    'Web': {
        'Url': 'http://...',
        'Port': 80
    }
}
print(type(dic))
print(dic)
print("IsTest" in dic)
print("DWHP" in dic)
print("Url" in dic)
print(dic['DbName'])

dic['quattro'] = 3
dic[5] = {
    'sub_item_1': '1',
    'sub_item_1': '2'
}

for i in dic:
    print(i)
for i in dic:
    print(f"{i}={dic[i]}")

import json
dic_2_json = json.dumps(dic)
new_dict = json.loads(dic_2_json)
print(dic_2_json)
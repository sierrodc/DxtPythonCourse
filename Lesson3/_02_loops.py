# -------------------------
# ---------- FOR ----------
# -------------------------
print("[1,2,3,4,5,6]")
for i in [1,2,3,4,5,6]:
    print(i)

print("range(1, 7, 1)")
for i in range(1, 7, 1):
    print(i)

print("range(1, 10, 2)")
for i in range(1, 10, 2):
    if i == 5:
        continue
    elif i == 7:
        break
    print(i)
else:
    print('uscito da for senza break')
print(i)

# -------------------------
# --------- WHILE ---------
# -------------------------
i = 0
while i < 10:
    print(i)
    i += 1 # i = i + 1
else:
    print('uscito da while senza break')

# -------------------------
# ----- COMPREHENSION -----
# -------------------------

a = range(1, 10)
print(type(a))
b = [x**2 for x in a if x % 2 == 0]
print(type(b))
print(b)
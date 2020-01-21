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
i = 1
res = []
while i < 10:
    if i % 2 == 0:
        res.append(i ** 2)
    print(i)
    i += 1 # i = i + 1
else:
    print('uscito da while senza break')


# ------------------------------
# ----- LIST COMPREHENSION -----
# ------------------------------
b = [x**2 for x in range(1, 10) if x % 2 == 0]
# similar to SQL:
# SELECT x^2
# FROM range(.) as x
# WHERE x%2=0
print(type(b))
print(b)
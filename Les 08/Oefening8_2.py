set1 = set()
for i in range(1, 1000):
    if i % 3 == 0:
        set1.add(i)
print(set1)

set2 = set()
for i in range(1, 1000):
    if i % 7 == 0:
        set2.add(i)
print(set2)


print(set1&set2) 	# opdracht a
print(set1|set2) 	# opdracht b
print(set1-set2)	# opdracht c

set3 = set()
for i in range(1, 1000):
    set3.add(i)
print(set3 - set1- set2)

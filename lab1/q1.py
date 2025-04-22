a = [x for x in range(0, 50)]
b = [y**2 for y in range(1, 51)]
c = [chr(z)*i for z, i in zip(range(97, 97+26+1), range(1, 27))]

print(a)
print()
print(b)
print()
print(c)

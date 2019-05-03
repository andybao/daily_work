def createGenerator():
    # yield (i*i for i in range(3))
    for i in range(3):
        return i * i

myGenerator = createGenerator()
print (myGenerator)
for i in myGenerator:
    print (i)
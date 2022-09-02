f = open("test.txt", "w+")

for i in range(5):
    f.write("Me estoy kgando de caloooooooooooooooor!\n".format(i+1))

f.close()

for line in open("test.txt", "r"):
    print(line)
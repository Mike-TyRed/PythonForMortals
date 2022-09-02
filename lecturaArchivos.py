f = open("test.txt", "r")

print(f.readline())
print(f.readline())
print(f.readline())

print(f.readline())
print(f.read())

f.close()

for line in open("test.txt", "r"):
    for i in line:
        print(i)
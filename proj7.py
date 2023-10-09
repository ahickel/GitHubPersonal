fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lines = line.split()
print(lines)

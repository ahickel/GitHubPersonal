fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.strip()
    if not line.startswith('From'):
        continue
    if not line.endswith('2008'):
        count = count + 1
        continue
    words = line.split()
    print(words[1])

print("There were", count, "lines in the file with From as the first word")

name = input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    line = line.strip()
    if not line.endswith('2008'):
        continue
    if line.startswith('From'):
        words = line.split()
        time = words[5]
        seperate_time = time.split(':')
        hours = seperate_time[0]
        counts[hours] = counts.get(hours,0)+1
lst = list()
for key, val in counts.items():
    newtup = (key,val)
    lst.append(newtup)
lst.sort()
for x,y in lst:
    print(x,y)
#only works for mbox-short.txt must have in same folder as py4e.

name = input("Enter file:")
handle = open(name)
counts = dict()
for line in handle:
    line = line.strip()
    if not line.endswith('2008'):
        continue
    if line.startswith('From'):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email,0)+1
email_name = None
email_count = None
for email, count in counts.items():
    if email_count is None or count > email_count:
        email_count = count
        email_name = email
print(email_name, email_count)
#file name is mbox-short.txt need to download into py4e for it to work

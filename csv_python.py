import csv

with open("test.csv", 'w',newline='') as f:
    writer = csv.writer(f)
    Header=['Name', 'cell', 'profession', 'Email']
    writer.writerow(Header)
    writer.writerow(['Brandon', '445 444 4444', 'Devops Engeneer', 'brandong@gmail.com'])

with open("python.txt", 'w') as f: # 'w' write , "r" read , 'a'apen
    f.write('this is the first line\n')
    f.write('this is the second line\n')   

with open('python.txt', 'r') as f1:
    f1.readline()
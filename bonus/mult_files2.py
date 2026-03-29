filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"{filename}", 'r')
    content = file.read()
    file.close()
    print(content)
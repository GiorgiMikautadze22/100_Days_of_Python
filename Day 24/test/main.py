with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('my_file.txt', mode='w') as file:
    file.write('gela magaria')

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('my_file.txt', mode='a') as file:
    file.write('\naba ra')

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)
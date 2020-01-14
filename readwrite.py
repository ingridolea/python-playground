


with open('name.txt') as f:
    my_name = f.read()

hi = "Hello, my name is "+ my_name

with open('hello.txt', 'w') as f:
    f.write(hi)
    f.write('\n')
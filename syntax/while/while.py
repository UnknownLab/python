def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Done!')

countdown(10)

while True:
    line = input('> ')
    if line == 'done':
     break
    print(line)

print('Done!')
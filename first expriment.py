import random
a = random.randint(1,10)
running = True
count = 0 
print('a small hint: my number area is one to ten')

while running and count < 3:
    number = int(input('please guess my nember: '))
    if number == a:
        print('victory!')
        break
    elif number > a:
        print('This number is too big')
    elif number < a:
        print('This number is too small')
    else :
        print('error')
    count += 1
else:
    print(f"result is {a}.Do you guess great?")

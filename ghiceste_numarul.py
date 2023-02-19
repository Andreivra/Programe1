import random
max = input('Introdu un numar:')
if max.isdigit():
    max = int(max)
    if max <= 0:
        print("Introduceti un numar mai mare de 0 data viitoare!!!!")
        quit()
else:
    print("Introduceti un numar data viitoare!!")
    quit()
r = random.randint(0, max)
introduceri = 0

while True:
    introduceri += 1
    user_guess = input("\nGhiceste numarul:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("\nIntroduceti un numar data viitoare!!")
        continue

    if user_guess == r:
        print('\nFelicitari!!! Ai ghicit numarul!')
        break
    elif user_guess > r:
        print("Numarul tau este mai mare!!!")
    else:
        print("Numarul tau este mai mic!!!")
print('\nAi ghicit din ', introduceri, ' incercari')

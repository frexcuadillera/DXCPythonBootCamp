from re import A

from numpy import not_equal

PIN = "1234"
USER_BALANCE = 1000

chances = 3

while chances > 0:
    pin_entry = input("Enter PIN: ")

    if PIN == pin_entry:
        print('pin matched')
    else:
        chances -= 1
        print('wrong PIN, ', chances, ' tries left')
        

print('account locked out')
exit()
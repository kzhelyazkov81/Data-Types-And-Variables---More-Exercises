n = int(input())
balanced = True
open = False


for _ in range (n):
    string = input()
    if string == '(' and not open:
        open = True
    elif string == '(' and open:
        balanced = False
        break
    if string == ')' and open:
        open = False
        balanced = True
    elif string == ')' and not open:
        balanced = False
        break

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

key = int(input())
n = int(input())
message = ''
for _ in range(n):
    letter = input()
    message += chr(ord(letter) + key)

print(message)

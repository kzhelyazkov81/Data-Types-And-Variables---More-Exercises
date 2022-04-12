number = int(input())
divisor = number // 2
prime = True

for i in range(1, divisor+1):
    if number % i == 0 and i != 1:
        prime = False

print(prime)

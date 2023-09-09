x, y, n = map(int,input().split())

numbers = [x, y]

if n == 1:
    print(min(numbers))
elif n == 2:
    print(max(numbers))

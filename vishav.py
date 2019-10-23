import sys
import demo


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


a = (int(input("Enter Number\n")))
i = 2
x = 0
if a <= 1:
    print("not prime")
    sys.exit()
while i <= int(a / 2):
    if a % i == 0:
        print("NOT PRIME")
        print(i)
        x = 1
        break
    i = i + 1
if x == 0:
    print("PRIME")
d = (int(input("Enter Factorial Number\n")))
c = fact(d)
print(c)
for x in demo.b:
    print(demo.b)

f = [2, 3, a]
a = {'v': 5, 'b': 2}
print(a['v'])
print(f)

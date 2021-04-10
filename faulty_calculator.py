print("Enter 1st no.")
num1 = int(input())
print("Enter 2st no.")
num2 = int(input())
print('What you want to calculate ?' + '+,-,*,%,/')
num3 = input()
if num1 == 45 and num2 == 3 and num3 == '*':
    print("556")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '*':
    mul = num1 * num2
    print(mul)
elif num3 == '+':
    sum = num1 + num2
    print(sum)
elif num3 == '/':
    div = num1 / num2
    print(div)
elif num3 == '%':
    mod = num1 % num2
    print(mod)
elif num3 == '-':
    sub = num1 - num2
    print(sub)
else:
    print("Please enter a valid argument")

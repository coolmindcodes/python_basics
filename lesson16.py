# Error handling
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
z = input("Enter Third Number: ")

try:
    x_num = int(x)
    y_num = int(y)
    z_num = int(z)
    print(x_num * y_num * z_num)
except:
    print("Enter valid numbers")
print("MENU\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\n5:Modulus\n6:Floor division\n7:Exponent\n8:Exit")
while True:
    op=int(input("Enter any choice\n"))
    match(op):
        case 1:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}+{b}={a+b}")
        case 2:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}-{b}={a-b}")
        case 3:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}*{b}={a*b}")
        case 4:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}/{b}={a/b}")
        case 5:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}%{b}={a%b}")
        case 6:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}//{b}={a//b}")
        case 7:
            a=int(input("Enter any number\n"))
            b=int(input("Enter any number\n"))
            print(f"{a}**{b}={a**b}")
        case 8:
            exit()
        case _:
            print("Invalid option")


username = "Vimi"
password = "123"

def validate():
    if username == uname and password == upass:
        return True
    else:
        return False

uname = input("Enter name:")
upass = input("Enter password:")
a=validate()
print(a)

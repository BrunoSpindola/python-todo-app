password = input("Enter new password: ")

result = {}

if len(password) < 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")

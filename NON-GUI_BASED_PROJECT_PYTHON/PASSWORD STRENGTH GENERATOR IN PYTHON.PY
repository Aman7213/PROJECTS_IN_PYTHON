import string

print("---PASSWORD STRENGTH CHECKER---")
password = input("Enter the password: ")

psl = len(password)
print(psl)
stren = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

if psl >= 8:
    for password in range (stren()):
        print("Password is Medium")
    else:
        print("Passwrod is Weak")
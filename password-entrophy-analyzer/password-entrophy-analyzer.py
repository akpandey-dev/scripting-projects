import math

password = input("Enter password: ")

charset = 0

if any(c.islower() for c in password):
    charset += 26

if any(c.isupper() for c in password):
    charset += 26

if any(c.isdigit() for c in password):
    charset += 10

if any(not c.isalnum() for c in password):
    charset += 32

entropy = len(password) * math.log2(charset if charset else 1)

print(f"\nEntropy: {entropy:.2f} bits")

if entropy < 28:
    print("Strength: Very Weak")
elif entropy < 36:
    print("Strength: Weak")
elif entropy < 60:
    print("Strength: Reasonable")
elif entropy < 128:
    print("Strength: Strong")
else:
    print("Strength: Uncrackable")
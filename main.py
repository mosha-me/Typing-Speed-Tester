import random
import string

a = int(input("Enter your password length: "))
b = string.ascii_letters + string.digits + string.punctuation
c = "".join(random.choice(b) for _ in range(a))

print("-" * 30)
print(f"your password: {c}")
print(f"password length: {len(c)} characters")
print("-" * 30)

if a < 8:
    print("WARNING: your password is too short! (use 8+)")
else:
    print("strong password")
    
    
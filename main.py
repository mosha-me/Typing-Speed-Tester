import time

print("type the following sentence exactly as shown:\n")
print("'python is super fun'\n")

input("press enter when you are ready to start...")
start = time.time()

typed = input("Type hear: ")

end = time.time()

Total_time = round(end - start, 2)

if typed == "python is super fun":
    print(f"\nGreat! Time taken {Total_time} second")
else:
    print("\nThe sentence didn't match. Try again! ")

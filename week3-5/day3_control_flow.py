temp = int(input("Enter the temperature: "))
if temp > 35:
    print("Hot")
elif temp >= 25:
    print("Warm")
else:
    print("Cool")


for i in range(1, 11):
    print(i*i)


c = 5
while c > 0:
    print(c)
    c -= 1
print("Blastoff!")


fruits=["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    if len(fruit) <= 5:
        continue  #the else isn't needed. continue already skips everything below it
    #else:
    print(fruit)
   





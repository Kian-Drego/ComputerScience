arr = []
print(arr)
demo = open("demo.txt", "r")

src = int(input("Enter the value you want to search: "))

for x in demo:
    arr.append(int(x))
    if int(x)==src:
        print("Number Found")
    else print("Number Not Found")
print(arr)


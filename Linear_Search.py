arr = []
demo = open("demo.txt", "r")

for x in demo:
    arr.append(int(x))
print(arr)

src = int(input("Enter the value you want to search: "))

flag = False
for x in arr:
    if int(x)==src:
        print("Number Found")
        flag = True

if flag == False:
    print("Number Not Found")

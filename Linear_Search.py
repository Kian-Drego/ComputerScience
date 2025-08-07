arr = []
demo = open("demo.txt", "r") # this opens the txt file

for x in demo:
    arr.append(int(x)) # append add the value of x to the next spot in the array
print(arr)

src = int(input("Enter the value you want to search: "))

flag = False # used instead of else, else statement would give repeated statement "Number not Found"
for x in arr:
    if int(x)==src:
        print("Number Found")
        flag = True

if flag == False:
    print("Number Not Found")

demo.close # closes the txt file

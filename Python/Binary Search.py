import random as rd

demo = open("demo.txt","r")
arr = []
for x in demo:
    arr.append(int(x))
demo.close()

n = len(arr)

for x in range(n-1): # can be avoided with arr.sort()
    if arr[x] > arr[x+1]:
        temp=arr[x]
        arr[x]=arr[x+1]
        arr[x+1]=temp
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
def search(arr, x):
    left = 0
    right = n-10

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


rnd = rd.randint(arr)
print(rnd)
print(search(arr, 4))

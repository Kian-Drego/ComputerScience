arr = []
print(arr)
demo = open("demo.txt", "r")

for x in demo:
    arr.append(int(x))
print(arr)

n = len(arr)

for x in range(n-1):
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

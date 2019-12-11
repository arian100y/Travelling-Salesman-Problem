
text = open("db2.txt", encoding="utf-8")
lines = []
j = 0
for i in text:

    test = i.split(",")
    if test[3]== "LOS OLIVOS":
        lines += [(float(test[5]),float(test[6]))]


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

quickSort(lines,0,len(lines)-1)


for i in range(len(lines)):
    print(lines[i])

write = open("testSET4.txt","w")
for i in lines:
    write.write(str(i[0])+","+str(i[1])+"\n")

print(len(lines))



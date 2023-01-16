n = 10
arr = [10, 4, 6, 5, 7, 8, 1, 3, 2, 6]
count = 0
for i in range (n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1
    print(arr)
print()
print(count, 'permutations')
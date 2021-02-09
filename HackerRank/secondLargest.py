n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
secondMax = min(arr)
for num in arr:
    if num > secondMax and num < mx:
        secondMax = num

print(secondMax)
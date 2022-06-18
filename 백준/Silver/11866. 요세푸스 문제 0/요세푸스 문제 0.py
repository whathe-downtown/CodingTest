a, b = map(int, input().split())  # 7 3
arr = [x for x in range(1, a + 1)]
idx = 0
answer = []
while len(arr) > 0:
    idx += (b-1)
    if idx > len(arr)-1:
        idx %= len(arr)
    answer.append(arr.pop(idx))
print('<'+ str(answer)[1:-1]+'>')
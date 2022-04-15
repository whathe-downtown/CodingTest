# 예제레르 입력받는다
a= int(input())
# if == 0 일때 List에서 가장 최근 리스트를 pop
list = []

for i in range(a):
    b = int(input())
    if b == 0:
        list.pop()
    else:
        list.append(b)

print(sum(list))




# 남은 리스트 배열을 for문을 돌려가면서 sum을 출력한다

n, k = map(int, input().split(' '))
second = ["+1", "-1", "*2"]
count = 0

def reindex(i, second):
    if i > len(second):
        i -= len(second)
        return i

def move(n, k, second, count, result): # 만약 n 이 k 의 2배라면 *2 해준다

    result += n
    while True:
        if n == k:
            break
        for i in second:
            i = reindex(i, second)
            result += eval[i]
            n += eval[i]

    move

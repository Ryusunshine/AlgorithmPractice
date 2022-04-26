n = int(input())
# n = 개수
box = [0] * n+1

def make_zero(n):
    if n<1:
        return
    box += make_zero()


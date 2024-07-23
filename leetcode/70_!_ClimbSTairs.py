# This is Fibonacci question, need to solve similiar
# problems about once at 1-2 weeks

def climbStairs(n: int) -> int:
    n1, n2 = 1, 2
    for i in range(n-1):
        n1, n2 = n2, n1 + n2
    return n1
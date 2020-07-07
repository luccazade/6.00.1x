def count7(N, count = 0):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return count
    else:
        if N % 10 == 7:
            count += 1
        N = N // 10
        return count7(N, count = count)

print(count7(8989))

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    def shallow_reverse(L):
        j = len(L) - 1
        for i in range(len(L) // 2):
            L[i], L[j] = L[j], L[i]
            j -= 1
        return L
    shallow_reverse(L)
    for i in L:
        shallow_reverse(i)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def specific_poly(value):
        total = 0
        length = len(L)
        for i in L:
            total += i * value ** (length - 1)
            length -= 1
        return total
    return specific_poly


print(general_poly([0,1.1,-1])(-10.2))


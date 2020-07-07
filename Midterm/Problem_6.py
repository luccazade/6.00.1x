def max_val(t, delistedInts = []):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # if len(t) == 1 and type(t) == tuple:
    #     print('hi')
    for i in t:
        if type(i) == int:
            delistedInts.append(i)
        else:
            max_val(i)
    return max(delistedInts)




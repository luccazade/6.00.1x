def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    # initialise list
    runs = []
    # initialise list of lists with each digit starting a new list
    for i in range(len(L)):
        runs.append([L[i]])
    for i in range(len(L)):
        if i >= len(L) - 1:
            break
        else:
            # Decide whether list will be increasing or decreasing
            j = i
            while True:
                increasing = False
                try:
                    if L[j + 1] > L[i]:
                        increasing = True
                        break
                    elif L[j + 1] < L[i]:
                        decreasing = True
                        break
                    else:
                        j += 1
                except IndexError:
                    increasing = True
                    break
        x = i
        if increasing:
            while L[x + 1] >= L[x]:
                runs[i].append(L[x+1])
                x += 1
                if x == len(L) - 1:
                    break
        else:
            while L[x + 1] <= L[x]:
                runs[i].append(L[x+1])
                x += 1
                if x == len(L) - 1:
                    break
    runDetails = []
    maxLen = 0
    for i in range(len(runs)):
        runDetails.append([runs[i]])
        runDetails[i].append(len(runs[i]))
        runDetails[i].append(i)
        if runDetails[i][1] > maxLen:
            maxLen = runDetails[i][1]
            maxInd = runDetails[i][2]
    sumRun = sum(runDetails[maxInd][0])
    return sumRun

print(longest_run([5,5,5]))

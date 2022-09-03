def subsetSum(A, k, S): 
    global X
    current_sum = 0
    
    for i in range(len(X)):
        current_sum += X[i]*A[i]

    if k >= len(A):
        if current_sum == S:
            return True
        else:
            return False

    else:
        if current_sum + A[k] <= S:
            X[k] = 1
            if subsetSum(A, k+1, S):
                return True
        X[k] = 0
        return subsetSum(A, k+1, S)


A = [2, 1, 7, 4, 3]
X = [0]*len(A)
print(subsetSum(A, 0, 5))

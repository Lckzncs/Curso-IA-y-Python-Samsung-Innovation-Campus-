def bubbleSort(S,show=False):
    n = len(S)
    for i in range(n):
        if show:
            print(S)
        for j in range(0, n-i-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]

def selectionSort1(S,show=False):
    R = []
    while len(S) > 0:
        if show:
            print(R,S)
        smallest = S.index(min(S))
        R.append(S[smallest])
        S.pop(smallest)
    return R

def selectionSort2(S,show=False):
    n = len(S)
    for i in range(n-1):
        if show:
            print(S)
        smallest = i
        for j in range(i+1,n):
            if S[j] < S[smallest]:
                smallest = j
        S[i], S[smallest] = S[smallest], S[i]
    
def insertionSort1(S,show=False):
    R = []
    while len(S) > 0:
        if show:
            print(R, S)
        x = S.pop()
        j = len(R) - 1
        while j >= 0 and x < R[j]:
            j -= 1
        R.insert(j+1, x)
    return R

def insertionSort2(S,show=False):
    n = len(S)
    for i in range(1, n):
        if show:
            print(S)
        x = S[i]
        j = i-1
        while j >=0 and x < S[j] :
            S[j+1] = S[j]
            j -= 1
        S[j+1] = x

def mergeSort1(S, show = False):
    n = len(S)
    if n <= 1:
        return S.copy()  # Return a copy to avoid modifying the original list
    if show: 
        print(S)
    mid = n // 2  # División entera!!!!!
    L, R = S[:mid], S[mid:] # Divido en dos sublistas desordenadas
    L = mergeSort1(L, show)  # Ordeno la sublista izquierda
    R = mergeSort1(R, show)  # Ordeno la sublista derecha
    # Create a new list to store the result
    result = [0] * n
    merge1(result, L.copy(), R.copy())  # Pass copies to avoid modifying the original lists
    return result


def merge1(S, L, R):
    k = 0
    while len(L) > 0 and len(R) > 0:
        if L[0] <= R[0]:
            S[k] = L.pop(0)
        else:
            S[k] = R.pop(0)
        k += 1
    while len(L) != 0:
        S[k] = L.pop(0)
        k += 1
    while len(R) != 0:
        S[k] = R.pop(0)
        k += 1
    return S  # Return the merged list

def mergeSort2(S, low, high,show = False):
    if low < high:
        if show:
            print(S)
        mid = (low + high) // 2
        mergeSort2(S,low, mid, show)
        mergeSort2(S, mid+1, high, show)
        merge2(S,low,mid,high)

def merge2(S, low, mid, high):
    R = []
    i,j = low, mid+1
    while i <= mid and j <= high:
        if S[i] < S[j]:
            R.append(S[i])
            i += 1
        else:
            R.append(S[j])
            j += 1
        if i > mid:
            for k in range (j, high+1):
                R.append(S[j])
        else:
            for k in range(i, mid+1):
                R.append(S[i])
        for k in range(len(R)):
            S[low + k] = R[k]

def quickSort(S, low, high, show = False):
    if low < high:
        if show:
            print(S)
        pivot_point = partition(S, low, high)
        quickSort(S, low, pivot_point-1, show)
        quickSort(S, pivot_point + 1, high, show)

def partition(S, low, high, show = False):
    pivot = S[low]
    left, right = low +1, high
    while left < right:
        if show:
            print(S)
        while left <= right and S[left] <= pivot:
            left += 1
        while left <= right and S[right] >= pivot:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
    pivot_point = right
    S[low], S[pivot_point] = S[pivot_point], S[low]
    return pivot_point




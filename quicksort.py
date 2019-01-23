a = [2,8,7,1,3,5,6,4]

def quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)

        # divide
        quicksort(a, p, q-1)
        # divide
        quicksort(a, q+1, r)

        # no need to conquer because it's sorted in place

def partition(a,p,r):
    # make pivot the last element of the array
    x = a[r]
    i = p-1 # to prevent extra if/else
    for j in range(p, r):
        # if smaller, then swap with the left-most element of larger than pivot parition
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
            print(a) # print state

    # switch the pivot back
    a[i+1],a[r] = a[r], a[i+1]

    return i+1


if __name__ == "__main__":
    quicksort(a,0, len(a)-1)
    print(a)

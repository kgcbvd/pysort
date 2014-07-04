#Insertion Sort
def sortinsert(array):
    for j in xrange(1, len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0) and (array[i] > key):
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array

A = [0] * int(input("Set the number of elements: "))
print "------------------"
for i in range(len(A)):
    A[i] = int(input("Element " + str(i) + " = "))

print "Old array: " + str(A)
sortinsert(A)
print "New array: " + str(A)


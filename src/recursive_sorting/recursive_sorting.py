# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0 # arrA index
    b = 0 # arrB index
    counter = 0 # merged_arr index

    while a < len(arrA) and b < len(arrB): # looping until the end of either of the lists
        if arrA[a] < arrB[b]:
            merged_arr[counter] = arrA[a]
            a += 1
        
        else:
            merged_arr[counter] = arrB[b]
            b += 1
        
        counter += 1
    
    # now we have to take care of the leftover values after the while loop closes
    while a < len(arrA):
        merged_arr[counter] = arrA[a]
        a += 1
        counter += 1

    while b < len(arrB):
        merged_arr[counter] = arrB[b]
        b += 1
        counter += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    merged = []
    if len(arr) > 1:
        midpt = len(arr) // 2
        leftside = arr[:midpt]
        rightside = arr[midpt:]

        # Now we recurse the left and right 
        l = merge_sort(leftside)
        r = merge_sort(rightside)
        # This will continue until we have a series of single-element lists

        merged = merge(l, r)

        return merged

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # We need to make 2 sub-lists out of the arr list
    # We'll go start to mid and then mid+1 to end
    midstart = mid +1 # this is the start of the second sub-list

    # As these sub-lists should already be sorted, we just have to check 1 inequality for a completed sort
    if arr[mid] <= arr[midstart]:
        return arr
    
    else:
        while start <= mid and midstart <= end:
            if arr[start] < arr[midstart]: # if true, we can leave the value as is, no change necessary
                start += 1
            
            else: # if false, whether equal or opposite, we have to move some elements around
                # Note, list methods are not appropriate here and they would have O(n) time complexity
                counter = midstart
                element = arr[midstart]
                
                # we're going to move all the elements between start and midstart, inclusive one space to the right
                while counter != start:
                    arr[counter] = arr[counter -1]
                    counter -= 1

                # and then replace the element at index 'start' with the element previously at index midstart
                arr[start] = element
                
                # and now we move all our variables, other than end, up one
                start += 1
                mid += 1
                midstart += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # with l being the left bound of the array and r being the right
    # there is only one edge case, l = r, and leaving the return 
    # outside of the loop will take care of that case
    if l < r:
        m = int((l + r) / 2)
        # now we have to recurse with each sub-list
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)

        # and now we call our helper function
        merge_in_place(arr, l, m, r)
        
    # and our return is outside of the loop as stated above
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


# a = [1, 3, 5, 8, 9]
# b = [2, 4, 6]
# print(merge(a, b)) # works!

myList = [54,26,93,17,77,31,44,55,20]
print(merge_sort(myList))
# bubble sort logic
def bubble_sort(c):
    """
    :param c:
    :return:
    """

    # loop till less than length of aaray c - 1
    for i in range(len(c) - 1):
        swapped  = False
        for j in range(len(c) - i - 1):

            # comparing if  current element is greater than element or not
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]
                swapped = True

        # if no elemet in the list is swapped then break the loop
        if not swapped:
            break
    return c

if __name__ == "__main__":
    try:
        print("Enter Number:")
        array = list(map(int, input().strip().split()))
        print("Array is:", array)
        print("Bubble sorted:", bubble_sort(array))
    except Exception as ex:
        print(ex)













    # c = [8,9,5,3,2,7,6,4,0,1,10]
    # print("Array is : ", c)
    # print("Bubble Sorted Array is:", bubble_sort(c))
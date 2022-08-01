# Selection sort in Python
import  logging
logging.basicConfig(filename='selection_sort.log',level = logging.DEBUG,filemode='a')

def selection_Sort(array, size):

    """
    :param array:
    :param size:
    :return:
    """
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selection_Sort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

if __name__ == "__main__":
    try:
        term = int(input())
        selection_Sort(term)
    except Exception as ex:
        logging.exception(ex)
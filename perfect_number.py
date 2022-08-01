# Python program to check Perfect Number

# Function to check perfect number

import  logging
logging.basicConfig(filename='mergesort.log',level = logging.DEBUG,filemode='a')

def is_perfect(num):
    """

    :param num:
    :return:
    """
    perfect_sum = 0

    for i in range(1, num):
        if num % i == 0:
            perfect_sum += i

    # Function call & Decision
    if perfect_sum == num:
        print('%d is PERFECT' % (num))
        logging.info("hi")
    else:
        print('%d is NOT PERFECT' % (num))


if __name__ == "__main__":
    try:
        integer = int(input(" Number: "))
        is_perfect(integer)
    except Exception as ex:
        logging.exception(ex)
        print(ex)
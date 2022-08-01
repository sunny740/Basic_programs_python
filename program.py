import  logging
logging.basicConfig(filename='Program.log',level = logging.DEBUG,filemode='a')

def add_two_numbers(a, b):

    """
    this function for adding two numbers
    :param a:
    :param b:
    :return:
    """
    a = 10
    b = 10
    c = a+b
    print(c)
    logging.info('hi')
    return c



if __name__ == "__main__":
    c = add_two_numbers(10, 20)
    print(c)
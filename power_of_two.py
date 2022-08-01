import  logging
logging.basicConfig(filename='powerof_two.log',level = logging.DEBUG,filemode='a')

def power_of_two(pow):
    for i in range(0, pow+1):
        print(5 ** i)


if __name__ == "__main__":
    try:
            # print(("Enter The Number: "))
            logging.info("Enter your Number")
            number = int(input())
            print(("Power of Two Numbers Are: "))
            power_of_two(number)
    except Exception as ex:
        logging.exception(ex)
        # print(ex)


# def is_power_of_two(number : int) -> bool:
#     while number != 1:
#         if number % 2:
#             return  False
#         number /= 2
#     return True

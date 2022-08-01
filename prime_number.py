def is_prime(num):
    """

    :param num:
    :return:
    """
    for n in range(2, int(num // 2) + 1):
        if num % n == 0:
            return False
        return True

if __name__ == "__main__":
    try:
        # print("Enter your number")
        number = int(input("Enter your Number:"))
        print(is_prime(number))
    except Exception as ex:
        print(ex)

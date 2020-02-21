# import logging

def excludeD () :
    nums = list(range(1,10001))
    for i in nums:
        tmp_value = i
        while 1:
            if tmp_value > 10000:
                break
            else:
                tmp_value = d(tmp_value)
                try :
                    nums.remove(tmp_value)
                    # logging.warn(tmp_value)
                except ValueError:
                    # logging.error(tmp_value)
                    break
        print(i)


def d(n : int) -> int:
    sum_of_digit = sumOfDigit(n,0)
    return sum_of_digit + n


def sumOfDigit(n : int, sum : int) -> int:
    if (n == 0):
        return sum
    else:
        return sumOfDigit(n // 10, sum + (n%10))

excludeD()
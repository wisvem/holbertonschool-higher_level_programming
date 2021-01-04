#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resultList = []
    for i in range(list_length):
        result = 0
        try:
            result = int(my_list_1[i])/int(my_list_2[i])
        except IndexError:
            print("out of range")
        except ValueError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            resultList.append(result)
    return resultList

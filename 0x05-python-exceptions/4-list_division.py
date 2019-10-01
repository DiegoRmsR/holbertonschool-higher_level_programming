#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for counter in range(list_length):
        try:
            divr = my_list_1[counter] / my_list_2[counter]
        except TypeError:
            divr = 0
            print("wrong type")
        except ZeroDivisionError:
            divr = 0
            print("division by 0")
        except IndexError:
            divr = 0
            print("out of range")
        finally:
            new_list.append(divr)
    return(new_list)

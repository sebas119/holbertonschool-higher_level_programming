#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(0, list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
            new.append(ans)
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        except IndexError:
            print("out of range")
        finally:
            pass
    return new

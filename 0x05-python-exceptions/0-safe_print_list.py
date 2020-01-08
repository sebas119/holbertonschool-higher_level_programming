def safe_print_list(my_list=[], x=0):
    try:
        ans = 0
        for i in range(0, x):
            print(my_list[i], end='')
            ans += 1
        print()
    except:
        print()
    finally:
        return ans

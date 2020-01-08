def safe_print_division(a, b):
    try:
        ans = a / b
        print("Inside result: {:1.1f}".format(ans))
    except ZeroDivisionError:
        ans = None
        print("Inside result: None")
    finally:
        return ans

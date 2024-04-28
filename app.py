from calc_function import do_addition,do_subtraction
def main():
    user_input=input("please select your choice:\n 1.add \n 2.subtract \n")

    a=int(input("first number: "))
    b=int(input("second number: "))

    if user_input=="1":
        result=do_addition(a,b)
    if user_input=="2":
        result=do_subtraction(a,b)
    return result

if __name__=="__main__":
    print(main())        
    
from calc_function import do_addition,do_subtraction
from multi import do_multiplication
def main():
    user_input=input("please select your choice:\n 1.add \n 2.subtract \n 3.multiplication")

    a=int(input("first number: "))
    b=int(input("second number: "))

    if user_input=="1":
        result=do_addition(a,b)
    elif user_input=="2":
        result=do_subtraction(a,b)
    elif user_input=="3":
        result=do_multiplication(a,b)
    return result

if __name__=="__main__":
    print(main())        
    
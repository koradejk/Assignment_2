






from Arithmetic import *

if __name__=="__main__":
    no1 = int(input("Enter First No1:"))
    no2 = int(input("Enter First No2:"))

    addition_result = Add(no1,no2)
    print("Addition of {} & {} is {}".format(no1,no2,addition_result))

    subtraction_result = Sub(no1,no2)
    print("Subtraction of {} & {} is {}".format(no1,no2,subtraction_result))

    multiplication_result = Multi(no1,no2)
    print("Multiplication of {} & {} is {}".format(no1,no2,multiplication_result))

    division_result = Div(no1,no2)
    print("Division of {} & {} is {}".format(no1,no2,division_result))






def main():
    no=int(input("Enter the number:"))
    for i in range(1,no+1):
        print(*(no-i)*"* "*1)
    print()
    for i in range(no,0,-1):
        print("*  "*i)
if __name__=="__main__":
    main()
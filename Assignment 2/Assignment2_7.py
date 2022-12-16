def main():
    no=int(input("Enter the number:"))
    for i in range(no):
        for j in range(no):
            print(j+1,end="  ")
        print()
if __name__=="__main__":
    main()
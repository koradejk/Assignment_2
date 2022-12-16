def main():
    no=(input("Enter the number:"))
    print(len(str(no)))

 #########################################
    num=int(input("enter the number:"))
    count=0
    while num!=0:
        num//=10
        count +=1
    print("Number of digit:"+str(count))

if __name__=="__main__":
    main()
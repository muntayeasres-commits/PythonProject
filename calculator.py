while True:
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    choice=int(input('Choose an option: '))
    if choice < 1 or choice > 5:
        print("Invalid choice. Please select a valid option.")
        continue
    elif choice==5:
        print("Goodbye!")
        break
    else:
        num1=int(input('Enter first number:'))
        num2=int(input('Enter second number:'))
    if choice==1:
        print(num1,'+',num2,'=',num1+num2)
    elif choice==2:
        print(num1,'-',num2,'=',num1-num2)
    elif choice==3:
        print(num1,'*',num2,'=',num1*num2)
    elif choice==4:
        if num2==0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1,'/',num2,'=',num1/num2)
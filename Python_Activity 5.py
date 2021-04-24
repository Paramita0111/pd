##take input from user.Here "choice" & "result" is veriable. & "int"(integer) command useing for take user input of a integer type.
print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Floor division");
print("5. Division");
print("6. Exit");
choice=int(input("Enter your choice :- "));  
if(choice>=1 and choice<=5):
	print("Enter two numbers:");
	no1=int(input());
	no2=int(input());
if choice==1:
	result=no1+no2;
	print("Result of Addition = ",result);
elif choice==2:
	result=no1-no2;
	print("Result of Subtraction = ",result);
elif choice==3:
	result=no1*no2;
	print("Result of Multiplication = ",result);
elif choice==4:
	result=no1/no2;
	print("Result of Floor Division = ",result);
elif choice==5:
	result=no1//no2;
	print("Result of Division = ",result);
elif choice==6:
	exit();
else:
	print("Wrong input...||")

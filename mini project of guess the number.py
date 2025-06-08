import random
gnumber=random.randint(1,100)
while True: 
 print("------------------GUESS THE NUMBER---------------------")
 number=int(input("Enter the number beetween the 1 to 100 :"))
 if(number==gnumber):
    print("You win!!!")
    break
 elif(number<gnumber):
     print("your number is Too small, try bigger number......")
 else:
    print("Your number is Too big, try smaller number......")

 
print("-------------------Game Over---------------------------")


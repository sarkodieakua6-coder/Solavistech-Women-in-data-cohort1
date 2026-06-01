#SECTION 3: CONTROL FLOW
#1. AGE ELIGIBILITY CHECKER
print("AGE ELIGIBILITY CHECKER :")
age = int(input("Enter your age : "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")


#2.PASSWORD VALIDATORxx\]
 
print("PASSWORD VALIDATOR :")
password = input("Enter a password : ")
if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
else:
    print("Password is valid.")
    
    
    #3. GRADE CLASSIFICATION
print("GRADE CLASSIFICATION :")
grade = float(input("Enter your grade percentage : "))
if grade >= 90:
    print("You received an A.")
elif grade >= 80:
    print("You received a B.")
elif grade >= 70:
    print("You received a C.")
elif grade >= 60:
    print("You received a D.")
else:
    print("You received an F.")
    
    
#4. MULTIPLICATION TABLE
print("MULTIPLICATION TABLE :")
number = int(input("Enter a number to generate its multiplication table : "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
    
    #5. NUMBER GUESSING GAME
print("NUMBER GUESSING GAME :")
import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Guess a number between 1 and 100 : "))
    attempts += 1
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

    
    #6. CONTDOWN TIMER
print("COUNTDOWN TIMER :")
import time
seconds = int(input("Enter the number of seconds for the countdown : "))
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")

    
#7. ATM WITHDRAWAL SIMULATION
print("ATM WITHDRAWAL SIMULATION :")
balance = 1000.0
withdrawal_amount = float(input("Enter the amount to withdraw : "))
if withdrawal_amount > balance:
    print("Insufficient funds. Withdrawal denied.")
else:    balance -= withdrawal_amount
print(f"Withdrawal successful. Your new balance is : {balance}")
    
    
    #8. LOGIN SYSTEM
print("LOGIN SYSTEM :")
username = input("Enter your username : ")
password = input("Enter your password : ")
if username == "admin" and password == "password123":
    print("Login successful. Welcome, admin!")
else:    print("Login failed. Invalid username or password.")


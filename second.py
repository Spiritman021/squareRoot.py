x = float(input("Enter any no. to find the square root : "))
guess = x/2;
while ((abs(x-(guess*guess)))>0.000001)):
    guess=(guess+(x/guess))/2
print(guess)

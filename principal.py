

principal = int(input("Enter principal: ")) 
time = int(input("Enter the time: ")) 
rate = int(input("Enter the rate: ")) 

# Calculate interest and total
interest = (principal * rate * time) / 100
total_amount = principal + interest

# Print results
print("Simple interest is:", interest) 
print("The total amount is:", total_amount)

#######################################################################################################################################################
# 
# Name: Vaishnavi Vinod
# SID:740100579
# Exam Date:27/03/2025
# Module: programming for business analytics (BEMM458_J_2_202425)
# Github link for this assignment:  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
# SID: 740100579
sid_keys = [7, 9]  # First digit 7, last digit 9 of my SID number


# Initializing an empty list to store (start, end) positions
my_list = []

# using loop function and find command to get the start and end position of each of the items in the sentence
for key in sid_keys:
    word = key_comments[key]  
    start_pos = customer_feedback.find(word)  
    end_pos = start_pos + len(word)  
    my_list.append((start_pos, end_pos)) 

# to output the list
print(my_list)


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
first_two_digits = 74
# Insert last two digits of ID number here:
last_two_digits = 79
revenue = first_two_digits  # 74
operating_profit = last_two_digits  # 79
total_customers = first_two_digits  # 74
lost_customers = last_two_digits  # 79
total_orders = last_two_digits  # 79
# Write your code for Operating Profit Margin
# Function to calculate Operating Profit Margin
def operating_profit_margin(revenue, operating_profit):
    return (operating_profit / revenue) * 100 
# Write your code for Revenue per Customer
# Function to calculate Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    return total_revenue / total_customers 
# Write your code for Customer Churn Rate
# Function to calculate Customer Churn Rate
def customer_churn_rate(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100 
# Write your code for Average Order Value
# Function to calculate Average Order Value
def average_order_value(total_revenue, total_orders):
    return total_revenue / total_orders 


# Call your designed functions here
# Calculate metrics
opm = operating_profit_margin(revenue, operating_profit)
rpc = revenue_per_customer(revenue, total_customers)
ccr = customer_churn_rate(lost_customers, total_customers)
aov = average_order_value(revenue, total_orders)
print("Operating Profit Margin:", opm, "%")
print("Revenue per Customer:", rpc)
print("Customer Churn Rate:", ccr, "%")
print("Average Order Value:", aov)
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Given price and demand data
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Create and train the linear regression model
model = LinearRegression()
model.fit(prices, demand)

# Predict demand when price is £52
price_to_predict = np.array([[52]])
predicted_demand = model.predict(price_to_predict)[0]
print("Predicted demand at £52:", predicted_demand)

# Finding price to maximize revenue
predicted_demands = model.predict(prices)
revenues = prices.flatten() * predicted_demands
optimal_price = prices[np.argmax(revenues)][0]
print("Optimal price to maximize revenue:", optimal_price)

# Plot the regression line
plt.scatter(prices, demand, color='blue', label='Actual Data')
plt.plot(prices, model.predict(prices), color='red', label='Regression Line')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Price vs Demand Regression')
plt.legend()
plt.show()

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart
import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')

# Adding titles and labels
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend(["---"])
plt.grid(True)
plt.show()







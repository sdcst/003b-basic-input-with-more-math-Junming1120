#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
A = float(input("What is the price of your first items?:" ))
B = float(input("What is the price of your second items?:" ))
C = float(input("What is the price of your third items?:" ))
D = float(input("What is the price of your fourth items?:" ))
F = float(input("What is the price of your fifth items?:" ))
T = A+B+C+D+F
Tax = T*0.12
Tax = round(Tax,2)
G = T+Tax
G = round(G,2)
print(f"Your subtotal is $ {T} and your taxes total $ {Tax} for a total of $ {G}")

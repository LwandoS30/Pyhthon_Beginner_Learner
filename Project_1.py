""""The syst em will calculate the total price for the customer
  the change and vat """

#Variable declaration for calculations
import datetime
from time import strftime

VAT = 0.15

amountDue = 0.00
totalPrice = 0.00
change = 0.00
totalVat = 0.00

storeName = "ZYX"

print("")
print("################################")
print("Welcome to "+ storeName +" Store")
#variable declarations and assigning values to variables
cashiername = input("Please inter cashier name: ")
tillNumber = input("Provide till number: ")

amountBrought = input("Please provide amount brought forward by the customer: ") 
numItems = input("Please enter number of items to be bought: ")
Itemprice = input("Provide the item price: ")

print(amountDue)
print(VAT)



#convert everthing to float
"""float(amountDue)
float(amountBrought)
int(numItems)
float(Itemprice)
float(totalVat)
float(change)
float(totalPrice)"""


#declaring and assigning current date
d = datetime.datetime.now()

#Calculations
amountDue = int(numItems) * Itemprice

totalVat = float(amountDue) * float(VAT)
totalPrice = float(amountDue) + float(totalVat)
change = float(amountBrought) - float(totalPrice)

#Display out put
print("The amount due is: " + str(amountDue))
print("The VAT amount is: " + str(totalVat))
print("The total amount due is: " + str(totalPrice))
print("The change amount from money brought forward is: " + str(change))


print("Time: " + str(d))
print("Served by: " + str(cashiername) + "At till: "+ tillNumber)
print("Thank you for shopping with " + str(storeName))
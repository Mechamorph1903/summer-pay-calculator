"""

Author: Daniel Anorue

Program Title: Summer Savings

File Description:

A program used to calculate the user's gross income, taxes and net income.
Then, help them get the values for planned costs and left over income.

"""



print("\t\tSummer Pay Calculator")

payRate = float(input("What is your pay per hour? "))
#payRate = float(payRate)
weeklyHour = input("How many hours did you work per week? ")
totalHours = int(weeklyHour) * 5
grossInc = float(totalHours * payRate)
taxes = 0.2 * grossInc
netPay = grossInc - taxes

schoolClothes = 0.15 * netPay
schoolSupplies = 0.03 * netPay
savingsBonds = 0.15 * netPay
parentsContribution = savingsBonds*0.75

leftOver = netPay - schoolClothes - schoolSupplies - savingsBonds
print("********************************************************")

print("Information about your pay")
print("-----------------------------")

print(f"-->Gross Pay:\t${grossInc:>1.2f}")
print(f"-->Taxes Owed:\t${taxes:>1.2f}")
print(f"-->Net Pay:\t${netPay:>1.2f}")
print("------------------------------")
print(f"-->School Clothes Savings:\t${schoolClothes:>1.2f}")
print(f"-->School Supplies Savings:\t${schoolSupplies:>1.2f}")
print(f"-->Your Savings Bonds Cost:\t${savingsBonds:>1.2f}")
print(f"-->Parent Savings Bonds Contribution:\t${parentsContribution:>1.2f}")
print("------------------------------")
print(f"-->You have ${leftOver:>1.2f} left over")
print("------------------------------")
print("********************************************************")

input("Press enter to exit")
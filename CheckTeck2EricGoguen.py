# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    salary = 500
    dependant = 3
    provincialTax = float(salary / 100 * 6.0)
    federalTax = float(salary / 100 * 25.0)
    dependantTax = float(salary / 100 * 2 * 3)
    totalTax = float(provincialTax + federalTax + dependantTax)
    moneyAfterTax = float(salary - totalTax)
    print("the provincial tax deduction is: {0}" .format (provincialTax))
    print("the federal tax deduction is: {0}" .format(federalTax))
    print("the dependant deduction is: {0}" .format(dependantTax))
    print("the total tax deducted is: {0}" .format(totalTax))
    print("you made: {0} after tax" .format(moneyAfterTax))






    # YOUR CODE ENDS HERE

main()

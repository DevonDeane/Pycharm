#  Write a program to calculate persons taxes

# Rules (taxes.py)
#
# first 25,000 == tax free
# next 25,001 and 60,000 = 16%
# next 60,001 and 75,000 = 33.5%
# >=75,001 = 40%


def taxCalculator(salary):
    if salary <= 25000:
        tax = 0.0

    elif 25001 <= salary <= 60000:#salary > 25000 and salary <= 60000:
        #Don't tax first $25,000
        taxable = salary - 25000
        tax = taxable * 0.16

    elif salary > 60000 and salary <= 75000:
        # Don't tax first $25,000
        #taxable = salary - 25000

        tax = 60000 * 0.16

        taxable = salary - 60000
        tax += taxable * 0.335

    elif salary > 75000:

        tax = 60000 * 0.16
        tax+= (75000-60000) * 0.335
        tax+= (salary-75000) * 0.40

        # taxable = salary - 25000
        # tax = taxable * 0.16
        #
        # taxable = salary - 12000
        # tax += taxable * 0.335
        #
        # taxable = salary - 42000
        # tax += taxable * 0.40
    return tax

sal = int(input("Please enter your annual salary:"))
tax = taxCalculator(sal)

print('You owe a total of $',tax,'in taxes!')
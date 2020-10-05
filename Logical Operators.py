#AND Logical Operators
high_income = True
good_credit = True


if high_income and good_credit:
    print("Eligible for Loan \n")


high_income = True
good_credit = False


if high_income and good_credit:
    print("Eligible for Loan")
print("Increase your loyalty \n")


#OR Logical Operators
high_income = True
good_credit = True


if high_income or good_credit:
    print("Eligible for Loan \n")


# NOT Operators
good_credit = True
criminal_record = False


if good_credit and not criminal_record:
    print("Eligible for Loan and that's fine \n")








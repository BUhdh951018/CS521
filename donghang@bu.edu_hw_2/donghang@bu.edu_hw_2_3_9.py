#Financial application: payroll

name = input("Enter employee's name:")
hours = eval(input("Enter number of hours worked in a week:"))
pay_rate = eval(input("Enter hourly pay rate:"))
federal_tax = eval(input("Enter federal tax withholding rate:"))
state_tax = eval(input("Enter state tax withholding rate:"))

pay = hours * pay_rate
federal = pay * federal_tax
state = pay * state_tax
total = federal + state
net = pay - total

federal_tax = format(federal_tax, ".1%")
state_tax = format(state_tax, ".1%")

print("\n")
print("Employee Name:", name)
print("Hours Worked:", format(hours, ".1f"))
print("Pay Rate: $", format(pay_rate, ".2f"))
print("Gross Pay: $", format(pay, ".1f"))
print("Deductions:\n", "Federal Withholding (", federal_tax, "): $", format(federal, ".1f"))
print(" State Withholding (", state_tax, "): $", format(state, ".2f"))
print(" Total Deduction:", format(total, ".2f"))
print("Net Pay:", format(net, ".2f"))

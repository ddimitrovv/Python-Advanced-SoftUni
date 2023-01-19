# On the first line, you will receive a sequence of pizza orders.
# Each order contains a different number of pizzas, separated by comma and space ", ".
# On the second line, you will receive a sequence of employees with pizza-making capacities
# (how many pizzas an employee could make), separated by comma and space ", ".
# Your task is to check if all pizza orders are completed.
# To do that, you should take the first order and the last employee and see:
#     • If the number of pizzas in the order is less than or equal to the employee's pizza making capacity,
#       the order is completed. Remove both the order and the employee.
#     • If the number of pizzas in the order is greater than the employee's pizza making capacity,
#       the remaining pizzas from the order are going to be made by the next employees until the order is completed.
#         ◦ If there are no more employees to finish the order, consider it not completed.
#     • The restaurant does not take orders for more than 10 pizzas at once.
#     • If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee.
# You should keep track of the total pizzas that are being made.
# Input
#     • On the first line you will be given a sequence of pizza orders each represented as a number –
#       integers separated by comma and space ", "
#     • On the second line you will be given a sequence of employees with pizza-making capacities –
#       integers separated by comma and space ", "
# Output
#     • If all orders are successfully completed, print:
# All orders are successfully completed!
# Total pizzas made: {total count}
# Employees: {left employees joined by ", "}
#     • Otherwise, if you ran out of employees and there are still some orders left print:
# Not all orders are completed.
# Orders left: {left orders joined by ", "}
# Constraints
#     • You will always have at least one order and at least one employee
#     • All integers will be in range [-100, 100]
from collections import deque

orders = deque((int(x)) for x in input().split(', '))
employees = [(int(x)) for x in input().split(', ')]

pizzas_made = 0
while orders and employees:
    current_pizzas_made = 0
    order = orders.popleft()
    if order > 10 or order <= 0:
        continue
    employee = employees.pop()
    if employee <= 0:
        orders.appendleft(order)
        continue
    if employee >= order:
        current_pizzas_made = order
    else:
        current_pizzas_made = employee
        orders.appendleft(order - employee)

    pizzas_made += current_pizzas_made

if orders:
    print('Not all orders are completed.')
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
if orders:
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
if employees:
    print(f"Employees: {', '.join(str(x) for x in employees)}")

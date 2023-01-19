# You will be given two sequences of integers representing bowls of ramen and customers.
# Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer.
# Try to serve every customer with ramen until we have no more ramen or customers left:
#     • Each time the value of the ramen is equal to the value of the customer,
#       remove them both and continue with the next bowl of ramen and the next customer.
#     • Each time the value of the ramen is bigger than the value of the customer,
#       decrease the value of that ramen with the value of that customer and remove the customer.
#       Then try to match the same bowl of ramen (which has been decreased) with the next customer.
#     • Each time the customer's value is bigger than the value of the ramen bowl,
#       decrease the value of the customer with the value of the ramen bowl and remove the bowl.
#       Then try to match the same customer (which has been decreased) with the next bowl of ramen.
# Look at the examples provided for a better understanding of the problem.
# Input
#     • On the first line, you will receive integers representing the bowls of ramen,
#       separated by a single space and a comma ", ".
#     • On the second line, you will receive integers representing the customers,
#       separated by a single space and a comma ", ".
# Output
#     • If all customers are served, print: "Great job! You served all the customers."
#         ◦ Print all the left ramen bowls (if any) separated by comma and space in the format:
#           "Bowls of ramen left: {bowls of ramen left}"
#     • Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
#         ◦ Print all customers left separated by comma and space in the format "Customers left: {customers left}"

from collections import deque

bowls_of_ramen = list(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen[-1]
    current_customer = customers[0]
    if current_customer > current_bowl:
        bowls_of_ramen.pop()
        customers.appendleft(customers.popleft() - current_bowl)

    elif current_customer < current_bowl:
        customers.popleft()
        bowls_of_ramen.append(bowls_of_ramen.pop() - current_customer)

    elif current_customer == current_bowl:
        bowls_of_ramen.pop()
        customers.popleft()


if not customers:
    print("Great job! You served all the customers.")
elif not bowls_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
if customers:
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

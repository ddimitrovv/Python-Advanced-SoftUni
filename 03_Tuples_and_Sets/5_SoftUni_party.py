# There is a party at SoftUni. Many guests are invited,
# and there are two types of them: Regular and VIP.
# When a guest comes, check if they exist on any of the two reservation lists.
# On the first line, you will receive the number of guests – N.
# On the following N lines, you will be receiving their reservation codes.
# All reservation codes are 8 characters long, and all VIP numbers will start with a digit.
# Keep in mind that all reservation numbers must be unique.
# After that, you will be receiving guests who came to the party until you read the "END" command.
# In the end, print the number of guests who did not come to the party and their reservation numbers:
#     • The VIP guests must be first.
#     • Both the VIP and the Regular guests must be sorted in ascending order.

def is_vip(reservation_code):
    return reservation_code[0].isdigit()


n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

while True:
    guest = input()

    if guest == "END":
        break
    if is_vip(guest):
        vip_guests.remove(guest)
    else:
        regular_guests.remove(guest)

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]

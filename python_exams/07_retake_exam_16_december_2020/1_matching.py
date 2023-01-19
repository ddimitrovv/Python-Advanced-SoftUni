# First you will be given a sequence of integers representing males.
# Afterwards you will be given another sequence of integers representing females.
# You have to start from the first female and try to match it with the last male.
#     • If their values are equal, you have to match them and remove both of them.
#       Otherwise, you should remove only the female and decrease the value of the male by 2.
#     • If someone’s value is equal to or below 0, you should remove him/her from the records
#       before trying to match him/her with anybody.
#     • Special case - if someone’s value divisible by 25 without remainder,
#       you should remove him/her and the next person of the same gender
#       before trying to match them with anybody.
# You need to stop matching people when you have no more females or males.
# Input
#     • On the first line of input you will receive the integers, representing the males,
#       separated by a single space.
#     • On the second line of input you will receive the integers, representing the females,
#       separated by a single space.
# Output
#     • On the first line of output - print the number of successful matches:
#         ◦ "Matches: {matchesCount}"
#     • On the second line - print all males left:
#         ◦ If there are no males: "Males left: none"
#         ◦ If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
#     • On the third line - print all females left:
#         ◦ If there are no females: "Females left: none"
#         ◦ If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
# Constraints
#     • All the given numbers will be valid integers in the range [-100, 100].

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0
while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)

    elif female <= 0:
        males.append(male)

    elif male % 25 == 0:
        if not males:
            break
        else:
            males.pop()
            females.appendleft(female)

    elif female % 25 == 0:
        if not females:
            break
        else:
            females.popleft()
            males.append(male)

    elif male != female:
        male -= 2
        if male > 0:
            males.append(male)

    else:
        matches += 1

print(f'Matches: {matches}')
males_output = 'none' if not males else ', '.join(str(x) for x in reversed(males))
print(f'Males left: {males_output}')
females_output = 'none' if not females else ', '.join(str(x) for x in females)
print(f'Females left: {females_output}')

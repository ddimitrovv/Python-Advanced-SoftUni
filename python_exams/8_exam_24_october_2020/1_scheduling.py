# You are hired to create a program that implements SJF (The Shortest Job First).
# It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job)
# separated by comma and space ", ". On the second line you will be given the index of the job
# that we are interested in and want to know how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed.
# For more clarifications, see the examples below.
# Input
#     • On the first line you will receive numbers separated by ", "
#     • On the second line you will receive the index of the task you are interested in
# Output
#     • Single line: the clock-cycles that will pass until the task you are interested in is finished


#  ---------- first solution ----------

# tasks_cycles = [int(x) for x in input().split(', ')]
# wanted_task_index = int(input())
#
# clock_cycles = [x for x in tasks_cycles if x < tasks_cycles[wanted_task_index]]
# indices = [i for i, x in enumerate(tasks_cycles) if x == tasks_cycles[wanted_task_index]]
# cycles_to_add = [tasks_cycles[i] for i in indices if i <= wanted_task_index]
# result = sum(clock_cycles) + sum(cycles_to_add)
#
# print(result)

#  ---------- second solution ----------

# tasks_cycles = [int(x) for x in input().split(', ')]
# wanted_task_index = int(input())
#
# shorter_cycles = [x for x in tasks_cycles if x < tasks_cycles[wanted_task_index]]
# fifo = [x for i, x in enumerate(tasks_cycles)
#         if x == tasks_cycles[wanted_task_index] and i <= wanted_task_index]
# result = sum(shorter_cycles) + sum(fifo)
#
# print(result)

#  ---------- third solution ----------

tasks_cycles = [int(x) for x in input().split(', ')]
wanted_task_index = int(input())

wanted_task_cycles = [x for i, x in enumerate(tasks_cycles) if
                      (x == tasks_cycles[wanted_task_index] and i <= wanted_task_index) or
                      x < tasks_cycles[wanted_task_index]]
result = sum(wanted_task_cycles)

print(result)

#    Input                    Output
# 3, 1, 10, 1, 2                7
# 0
# 4, 10, 10, 6, 2, 99           32
# 2

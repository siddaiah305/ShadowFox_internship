import random

num_rolls = 20  

count_six = 0
count_one = 0
count_consecutive_sixes = 0

rolls = []


for _ in range(num_rolls):
    rolls.append(random.randint(1, 6))


for i in range(len(rolls)):
    print(f"Rolled: {rolls[i]}")  
    
    
    if rolls[i] == 6:
        count_six += 1
    if rolls[i] == 1:
        count_one += 1
    

    if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
        count_consecutive_sixes += 1


print("\nStatistics:")
print(f"Number of times rolled a 6: {count_six}")
print(f"Number of times rolled a 1: {count_one}")
print(f"Number of times rolled two 6s in a row: {count_consecutive_sixes}")

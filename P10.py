# P 10: Loss in business

minSkill = 100
skills = []
peoples = int(input("Enter number of people: "))
for i in range(peoples):
    push = int(input(f"Enter person {i+1} skill: "))
    skills.append(push) #because it is not taking push directly in list

for i in range(peoples):
    if skills[i] >= minSkill:
        print("Yes")
    else:
        print("No")    
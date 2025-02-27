justice_league=["Superman","Batmanat","Wonder Woman", "Flash", "Aquaman", "Green Lantern"] 
print(len(justice_league))#there are 6 members is present
justice_league.extend(["Batgirl","Nightwing"])
print(justice_league)
justice_league[0],justice_league[2]=justice_league[2],justice_league[0]#swapping method is used.
print(justice_league)
justice_league[-1],justice_league[-2]=justice_league[-2],justice_league[-1]
print(justice_league)
justice_league.clear()
# print(justice_league)
justice_league.extend(["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"])
print(justice_league)
justice_league_2=["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
sorted_justice_league=sorted(justice_league_2)
print(sorted_justice_league)
print(sorted_justice_league[0])
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"Your total expenses: {your_total}")
print(f"Your partner's total expenses: {partner_total}")

if your_total > partner_total:
    print("You spent more overall.")
elif your_total < partner_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

max_diff_category = max(your_expenses.keys(), key=lambda x: abs(your_expenses[x] - partner_expenses[x]))
max_diff = abs(your_expenses[max_diff_category] - partner_expenses[max_diff_category])

print(f"Biggest spending difference is in {max_diff_category} with a difference of {max_diff}.")

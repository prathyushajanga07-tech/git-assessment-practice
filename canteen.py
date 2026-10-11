menu = {
    "Samosa": 15,
    "Dosa": 40,
    "Tea": 12,
    "Idli": 30,
    "Coffee": 20,
    "Combo Meal": 60,
    "Lemon Soda": 25
}

print("Welcome to ACE Canteen!")
print("\n--- MENU ---")

for item, price in menu.items():
    print(f"{item}: Rs. {price}")

print("\nThank you for visiting!Visit again!")

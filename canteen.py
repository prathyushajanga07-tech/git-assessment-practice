menu = {
    "Samosa": 15,
    "Dosa": 40,
    "Tea": 10
}

print("Welcome to ACE Canteen!")
print("\n--- MENU ---")

for item, price in menu.items():
    print(f"{item}: Rs. {price}")

print("\nThank you for visiting!")

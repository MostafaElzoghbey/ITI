# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email or not


name = input("Enter your name: ").strip()

while not name.strip() or not name.isalpha():

    name = input("Please enter a valid name: ").strip()

email = input("Enter your email: ").strip()

while not "@" in email or not "." in email:

    email = input("Please enter a valid email: ").strip()

print("\nName:", name)
print("email:", email)


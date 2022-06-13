import random

choices = ["R", "P", "S"]

while True:
    random_index = random.randint(0, 2)
    cpu_choice = choices[random_index]

    user_choice = input("R, P, or S? ").upper()
    while user_choice not in choices:
        user_choice = input(
            "This input is invalid. Pick again: ").upper()

    print()
    print("PLAYER:", user_choice, "COMPUTER:", cpu_choice)

    if user_choice == 'R':
        if cpu_choice == 'R':
            print("It's a tie!")
        elif cpu_choice == 'S':
            print("You win!")

        elif cpu_choice == 'P':
            print("You lose!")

    elif user_choice == 'P':
        if cpu_choice == 'P':
            print("It's a tie!")
        elif cpu_choice == 'R':
            print("You win!")

        elif cpu_choice == 'S':
            print("You lose!")

    elif user_choice == 'S':
        if cpu_choice == 'S':
            print("It's a tie!")
        elif cpu_choice == 'P':
            print("You win!")

        elif cpu_choice == 'R':
            print("You lose!")
            # restarting the game from step 3

            continue

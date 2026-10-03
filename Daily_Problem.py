# Daily Problem Solver

problems = {
    "1": {
        "name": "Study",
        "keywords": ["study", "concentrate", "focus", "exam", "homework"],
        "solution": "Try studying for 25 minutes without using your phone, then take a 5-minute break."
    },
    "2": {
        "name": "Time Management",
        "keywords": ["time", "schedule", "busy", "manage", "procrastinate"],
        "solution": "Make a simple to-do list and complete the most important task first."
    },
    "3": {
        "name": "Stress",
        "keywords": ["stress", "stressed", "pressure", "worried", "worry"],
        "solution": "Take a short break, breathe slowly, and divide your problem into smaller tasks."
    },
    "4": {
        "name": "Sleep",
        "keywords": ["sleep", "tired", "sleepy", "insomnia", "rest"],
        "solution": "Try to maintain a regular sleep schedule and avoid using your phone before bed."
    },
    "5": {
        "name": "Exercise",
        "keywords": ["exercise", "fitness", "body", "workout", "active"],
        "solution": "Start with a simple 15–20 minute walk or light exercise each day."
    }
}


def show_menu():
    print("\n================================")
    print("       DAILY PROBLEM SOLVER")
    print("================================")

    for number, problem in problems.items():
        print(number + ".", problem["name"])

    print("6. Exit")


def find_solution(user_problem):
    user_problem = user_problem.lower()

    for problem in problems.values():
        for keyword in problem["keywords"]:
            if keyword in user_problem:
                return problem["name"], problem["solution"]

    return None, None


def solve_problem():
    user_problem = input("\nDescribe your problem: ")

    if user_problem.strip() == "":
        print("Please enter a problem.")
        return

    category, solution = find_solution(user_problem)

    if solution:
        print("\n--------------------------------")
        print("Problem Category:", category)
        print("--------------------------------")
        print("💡 Suggestion:")
        print(solution)
    else:
        print("\nSorry, I could not identify your problem.")
        print("Try describing it using words related to:")
        print("Study, time, stress, sleep, or exercise.")


while True:

    show_menu()

    choice = input("\nEnter your choice: ")

    if choice == "6":
        print("\nThank you for using Daily Problem Solver!")
        print("Keep learning and keep improving. 🚀")
        break

    elif choice in problems:
        print("\nYou selected:", problems[choice]["name"])
        solve_problem()

    else:
        print("\nInvalid choice!")
        print("Please choose a number from 1 to 6.")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for using Daily Problem Solver! 👋")
        break
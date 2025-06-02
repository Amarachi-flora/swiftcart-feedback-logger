import datetime

feedback_file = "customer_feedback.txt"

def save_feedback(name, message):
    today = datetime.date.today()
    try:
        with open(feedback_file, "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Feedback: {message}\n")
            file.write(f"Date: {today}\n")
            file.write("---\n")
        print("\n Feedback saved successfully!\n")
    except Exception as e:
        print(f"\n Error saving feedback: {e}\n")

def view_all_feedback():
    try:
        with open(feedback_file, "r") as file:
            content = file.read()
            if content.strip():
                print("\n Customer Feedback:\n")
                print(content)
            else:
                print("\n No feedback yet. Be the first!\n")
    except FileNotFoundError:
        print("\n Feedback file not found. Add some feedback first.\n")

def main():
    while True:
        print("\nWelcome to SwiftCart Feedback Logger")
        print("1. Add New Feedback")
        print("2. View All Feedback")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter your name: ").strip()
            message = input("Enter your feedback: ").strip()

            if not name or not message:
                print("\n⚠ Please provide both name and feedback.\n")
            else:
                save_feedback(name, message)

        elif choice == "2":
            view_all_feedback()

        elif choice == "3":
            print("\n Thank you for using SwiftCart Feedback Logger. Goodbye.\n")
            break

        else:
            print("\n Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()

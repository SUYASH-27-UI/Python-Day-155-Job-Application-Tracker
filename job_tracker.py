
import json
import os

FILE_NAME = "applications.json"


def load_applications():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Unable to read application data.")
        return []


def save_applications(applications):
    with open(FILE_NAME, "w") as file:
        json.dump(applications, file, indent=4)


def add_application(applications):
    company = input("Enter company name: ").strip()
    role = input("Enter job role: ").strip()
    location = input("Enter job location: ").strip()

    if not company or not role or not location:
        print("All fields are required.")
        return

    application_id = max(
        (item["id"] for item in applications),
        default=1000
    ) + 1

    application = {
        "id": application_id,
        "company": company,
        "role": role,
        "location": location,
        "status": "Applied"
    }

    applications.append(application)
    save_applications(applications)

    print(f"Application added! ID: {application_id}")


def view_applications(applications):
    if not applications:
        print("No applications available.")
        return

    print("\n--- JOB APPLICATIONS ---")

    for app in applications:
        print(
            f"ID: {app['id']} | "
            f"Company: {app['company']} | "
            f"Role: {app['role']} | "
            f"Location: {app['location']} | "
            f"Status: {app['status']}"
        )


def search_application(applications):
    company = input("Enter company name: ").strip().lower()

    results = [
        app for app in applications
        if company in app["company"].lower()
    ]

    if not results:
        print("No matching application found.")
        return

    for app in results:
        print(
            f"ID: {app['id']} | {app['company']} | "
            f"{app['role']} | {app['status']}"
        )


def update_status(applications):
    try:
        application_id = int(input("Enter application ID: "))
    except ValueError:
        print("Invalid application ID.")
        return

    for app in applications:
        if app["id"] == application_id:
            print("1. Applied")
            print("2. Interview")
            print("3. Selected")
            print("4. Rejected")

            choice = input("Choose new status: ")

            statuses = {
                "1": "Applied",
                "2": "Interview",
                "3": "Selected",
                "4": "Rejected"
            }

            if choice not in statuses:
                print("Invalid status.")
                return

            app["status"] = statuses[choice]
            save_applications(applications)

            print("Application status updated.")
            return

    print("Application not found.")


def show_summary(applications):
    print("\n--- APPLICATION SUMMARY ---")

    statuses = ["Applied", "Interview", "Selected", "Rejected"]

    for status in statuses:
        count = sum(
            1 for app in applications
            if app["status"] == status
        )

        print(f"{status}: {count}")


def main():
    applications = load_applications()

    while True:
        print("\n===== JOB APPLICATION TRACKER =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Company")
        print("4. Update Status")
        print("5. Application Summary")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            search_application(applications)
        elif choice == "4":
            update_status(applications)
        elif choice == "5":
            show_summary(applications)
        elif choice == "6":
            print("Job tracker closed.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

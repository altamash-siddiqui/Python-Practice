import sqlite3
from datetime import datetime


DATABASE_NAME = "tasks.db"


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

def connect_database():
    return sqlite3.connect(DATABASE_NAME)


# --------------------------------------------------
# CREATE TABLE
# --------------------------------------------------

def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending',
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# --------------------------------------------------
# ADD TASK
# --------------------------------------------------

def add_task():
    print("\n" + "-" * 50)
    print("ADD NEW TASK")
    print("-" * 50)

    title = input("Task title: ").strip()

    if not title:
        print("❌ Task title cannot be empty.")
        return

    description = input("Description: ").strip()

    priority = input(
        "Priority (Low / Medium / High): "
    ).strip().capitalize()

    if priority not in ["Low", "Medium", "High"]:
        priority = "Medium"

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, description, priority, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        description,
        priority,
        "Pending",
        created_at
    ))

    connection.commit()
    connection.close()

    print("\n✅ Task added successfully.")


# --------------------------------------------------
# VIEW TASKS
# --------------------------------------------------

def view_tasks():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, priority, status, created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    connection.close()

    print("\n" + "=" * 75)
    print("                         ALL TASKS")
    print("=" * 75)

    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        task_id, title, priority, status, created_at = task

        print(
            f"\nID: {task_id}"
            f"\nTask: {title}"
            f"\nPriority: {priority}"
            f"\nStatus: {status}"
            f"\nCreated: {created_at}"
        )

        print("-" * 50)


# --------------------------------------------------
# UPDATE TASK STATUS
# --------------------------------------------------

def complete_task():
    view_tasks()

    try:
        task_id = int(
            input("\nEnter task ID to complete: ")
        )
    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, ("Completed", task_id))

    if cursor.rowcount == 0:
        print("❌ Task not found.")
    else:
        print("✅ Task marked as completed.")

    connection.commit()
    connection.close()


# --------------------------------------------------
# DELETE TASK
# --------------------------------------------------

def delete_task():
    view_tasks()

    try:
        task_id = int(
            input("\nEnter task ID to delete: ")
        )
    except ValueError:
        print("❌ Please enter a valid ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    if cursor.rowcount == 0:
        print("❌ Task not found.")
    else:
        print("🗑️ Task deleted successfully.")

    connection.commit()
    connection.close()


# --------------------------------------------------
# SEARCH TASK
# --------------------------------------------------

def search_task():
    keyword = input(
        "\nEnter keyword to search: "
    ).strip()

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, priority, status
        FROM tasks
        WHERE title LIKE ?
           OR description LIKE ?
        ORDER BY id DESC
    """, (
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    results = cursor.fetchall()

    connection.close()

    print("\n" + "=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    if not results:
        print("🔍 No matching tasks found.")
        return

    for task in results:
        task_id, title, priority, status = task

        print(
            f"\nID: {task_id}"
            f"\nTask: {title}"
            f"\nPriority: {priority}"
            f"\nStatus: {status}"
        )

        print("-" * 40)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def show_menu():
    print("\n" + "=" * 60)
    print("              🚀 SMART TASK MANAGER")
    print("=" * 60)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    print("=" * 60)


def main():

    create_table()

    while True:

        show_menu()

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            search_task()

        elif choice == "6":
            print("\n👋 Task Manager closed.")
            break

        else:
            print("\n❌ Invalid choice. Try again.")


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------

if __name__ == "__main__":
    main()
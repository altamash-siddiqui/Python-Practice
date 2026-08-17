import sqlite3
from datetime import datetime, date


# ============================================================
# CONFIGURATION
# ============================================================

DATABASE_NAME = "tasks.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_database():
    return sqlite3.connect(DATABASE_NAME)


# ============================================================
# CREATE DATABASE TABLE
# ============================================================

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
            due_date TEXT,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ============================================================
# ADD TASK
# ============================================================

def add_task():

    print("\n" + "-" * 60)
    print("                    ADD NEW TASK")
    print("-" * 60)

    title = input("Task title: ").strip()

    if not title:
        print("❌ Task title cannot be empty.")
        return

    description = input("Description: ").strip()

    print("\nPriority Options:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Choose priority: ").strip()

    priority_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    priority = priority_map.get(
        priority_choice,
        "Medium"
    )

    due_date = input(
        "\nDue date (YYYY-MM-DD): "
    ).strip()

    if due_date:

        try:
            datetime.strptime(
                due_date,
                "%Y-%m-%d"
            )

        except ValueError:

            print(
                "❌ Invalid date format."
                "\nUse YYYY-MM-DD."
            )

            return

    else:

        due_date = None

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (
            title,
            description,
            priority,
            status,
            due_date,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        description,
        priority,
        "Pending",
        due_date,
        created_at
    ))

    connection.commit()
    connection.close()

    print("\n✅ Task added successfully.")


# ============================================================
# VIEW ALL TASKS
# ============================================================

def view_tasks():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            description,
            priority,
            status,
            due_date,
            created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    connection.close()

    print("\n" + "=" * 80)
    print("                         ALL TASKS")
    print("=" * 80)

    if not tasks:

        print("📭 No tasks found.")
        print("=" * 80)

        return

    for task in tasks:

        print(f"\n🆔 ID          : {task[0]}")
        print(f"📌 Title       : {task[1]}")
        print(
            f"📝 Description : "
            f"{task[2] or 'No description'}"
        )
        print(f"🔥 Priority    : {task[3]}")
        print(f"📊 Status      : {task[4]}")
        print(
            f"📅 Due Date    : "
            f"{task[5] or 'No deadline'}"
        )
        print(f"🕒 Created     : {task[6]}")

        print("-" * 80)


# ============================================================
# UPDATE TASK
# ============================================================

def update_task():

    view_tasks()

    try:

        task_id = int(
            input("\nEnter task ID to update: ")
        )

    except ValueError:

        print("❌ Invalid task ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            title,
            description,
            priority,
            due_date
        FROM tasks
        WHERE id = ?
    """, (task_id,))

    task = cursor.fetchone()

    if not task:

        print("❌ Task not found.")
        connection.close()
        return

    old_title = task[0]
    old_description = task[1]
    old_priority = task[2]
    old_due_date = task[3]

    print(
        "\nPress Enter to keep existing value."
    )

    new_title = input(
        f"Title [{old_title}]: "
    ).strip()

    new_description = input(
        f"Description "
        f"[{old_description or 'None'}]: "
    ).strip()

    new_priority = input(
        f"Priority [{old_priority}] "
        f"(Low/Medium/High): "
    ).strip().capitalize()

    new_due_date = input(
        f"Due Date "
        f"[{old_due_date or 'None'}] "
        f"(YYYY-MM-DD): "
    ).strip()

    if not new_title:
        new_title = old_title

    if not new_description:
        new_description = old_description

    if new_priority not in [
        "Low",
        "Medium",
        "High"
    ]:
        new_priority = old_priority

    if not new_due_date:

        new_due_date = old_due_date

    else:

        try:

            datetime.strptime(
                new_due_date,
                "%Y-%m-%d"
            )

        except ValueError:

            print("❌ Invalid date format.")
            connection.close()
            return

    cursor.execute("""
        UPDATE tasks
        SET
            title = ?,
            description = ?,
            priority = ?,
            due_date = ?
        WHERE id = ?
    """, (
        new_title,
        new_description,
        new_priority,
        new_due_date,
        task_id
    ))

    connection.commit()
    connection.close()

    print("\n✅ Task updated successfully.")


# ============================================================
# COMPLETE TASK
# ============================================================

def complete_task():

    view_tasks()

    try:

        task_id = int(
            input("\nEnter task ID to complete: ")
        )

    except ValueError:

        print("❌ Invalid task ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (
        "Completed",
        task_id
    ))

    if cursor.rowcount == 0:

        print("❌ Task not found.")

    else:

        print("✅ Task marked as completed.")

    connection.commit()
    connection.close()


# ============================================================
# DELETE TASK
# ============================================================

def delete_task():

    view_tasks()

    try:

        task_id = int(
            input("\nEnter task ID to delete: ")
        )

    except ValueError:

        print("❌ Invalid task ID.")
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


# ============================================================
# SEARCH TASK
# ============================================================

def search_task():

    keyword = input(
        "\nEnter keyword to search: "
    ).strip()

    if not keyword:

        print("❌ Keyword cannot be empty.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            description,
            priority,
            status,
            due_date
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

    print("\n" + "=" * 70)
    print("                       SEARCH RESULTS")
    print("=" * 70)

    if not results:

        print("🔍 No matching tasks found.")
        return

    for task in results:

        print(f"\n🆔 ID          : {task[0]}")
        print(f"📌 Title       : {task[1]}")
        print(
            f"📝 Description : "
            f"{task[2] or 'No description'}"
        )
        print(f"🔥 Priority    : {task[3]}")
        print(f"📊 Status      : {task[4]}")
        print(
            f"📅 Due Date    : "
            f"{task[5] or 'No deadline'}"
        )

        print("-" * 70)


# ============================================================
# TASK STATISTICS
# ============================================================

def show_statistics():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM tasks"
    )

    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Completed'
    """)

    completed = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Pending'
    """)

    pending = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE priority = 'High'
    """)

    high = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE priority = 'Medium'
    """)

    medium = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE priority = 'Low'
    """)

    low = cursor.fetchone()[0]

    connection.close()

    completion_rate = (
        (completed / total) * 100
        if total > 0
        else 0
    )

    print("\n" + "=" * 70)
    print("                     TASK STATISTICS")
    print("=" * 70)

    print(f"📋 Total Tasks       : {total}")
    print(f"✅ Completed         : {completed}")
    print(f"⏳ Pending           : {pending}")

    print("\nPriority Breakdown")
    print("-" * 40)

    print(f"🔴 High              : {high}")
    print(f"🟡 Medium            : {medium}")
    print(f"🟢 Low               : {low}")

    print("\n📈 Completion Rate   : "
          f"{completion_rate:.1f}%")

    print("=" * 70)


# ============================================================
# OVERDUE TASKS
# ============================================================

def show_overdue_tasks():

    today = date.today().isoformat()

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            description,
            priority,
            due_date
        FROM tasks
        WHERE due_date IS NOT NULL
          AND due_date < ?
          AND status != 'Completed'
        ORDER BY due_date ASC
    """, (today,))

    tasks = cursor.fetchall()

    connection.close()

    print("\n" + "=" * 75)
    print("                    ⚠️ OVERDUE TASKS")
    print("=" * 75)

    if not tasks:

        print("🎉 No overdue tasks!")
        return

    for task in tasks:

        print(f"\n🆔 ID          : {task[0]}")
        print(f"📌 Title       : {task[1]}")
        print(
            f"📝 Description : "
            f"{task[2] or 'No description'}"
        )
        print(f"🔥 Priority    : {task[3]}")
        print(f"📅 Due Date    : {task[4]}")
        print("⚠️ Status      : OVERDUE")

        print("-" * 75)


# ============================================================
# PRODUCTIVITY DASHBOARD
# ============================================================

def productivity_dashboard():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM tasks"
    )
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Completed'
    """)
    completed = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Pending'
    """)
    pending = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE priority = 'High'
    """)
    high = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE due_date IS NOT NULL
          AND due_date < ?
          AND status != 'Completed'
    """, (date.today().isoformat(),))

    overdue = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE due_date = ?
          AND status != 'Completed'
    """, (date.today().isoformat(),))

    today_tasks = cursor.fetchone()[0]

    connection.close()

    completion_rate = (
        (completed / total) * 100
        if total > 0
        else 0
    )

    print("\n" + "=" * 75)
    print("                 🚀 PRODUCTIVITY DASHBOARD")
    print("=" * 75)

    print("\nTASK OVERVIEW")
    print("-" * 45)

    print(f"📋 Total Tasks       : {total}")
    print(f"⏳ Pending           : {pending}")
    print(f"✅ Completed         : {completed}")
    print(f"⚠️ Overdue           : {overdue}")
    print(f"📅 Due Today         : {today_tasks}")

    print("\nPRIORITY")
    print("-" * 45)

    print(f"🔴 High Priority     : {high}")

    print("\nPRODUCTIVITY")
    print("-" * 45)

    print(
        f"📈 Completion Rate   : "
        f"{completion_rate:.1f}%"
    )

    if completion_rate >= 80:

        print(
            "🔥 Excellent productivity!"
        )

    elif completion_rate >= 50:

        print(
            "🚀 Good progress. Keep going!"
        )

    elif completion_rate > 0:

        print(
            "💪 Keep pushing. You are improving!"
        )

    else:

        print(
            "🌱 Start completing your tasks!"
        )

    print("=" * 75)


# ============================================================
# MENU
# ============================================================

def show_menu():

    print("\n" + "=" * 75)
    print("                  🚀 SMART TASK MANAGER")
    print("=" * 75)

    print("1. ➕ Add Task")
    print("2. 📋 View All Tasks")
    print("3. ✅ Complete Task")
    print("4. 🗑️ Delete Task")
    print("5. ✏️ Update Task")
    print("6. 🔎 Search Task")
    print("7. 📊 Task Statistics")
    print("8. ⚠️ Overdue Tasks")
    print("9. 🚀 Productivity Dashboard")
    print("10. 🚪 Exit")

    print("=" * 75)


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():

    create_table()

    print("\n" + "=" * 75)
    print("             WELCOME TO SMART TASK MANAGER")
    print("=" * 75)

    while True:

        show_menu()

        choice = input(
            "\nChoose an option (1-10): "
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
            update_task()

        elif choice == "6":
            search_task()

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            show_overdue_tasks()

        elif choice == "9":
            productivity_dashboard()

        elif choice == "10":

            print("\n" + "=" * 75)
            print(
                "👋 Thank you for using "
                "Smart Task Manager!"
            )
            print(
                "🚀 Keep building. Keep learning."
            )
            print("=" * 75)

            break

        else:

            print(
                "\n❌ Invalid choice."
                "\nPlease select an option between 1 and 10."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
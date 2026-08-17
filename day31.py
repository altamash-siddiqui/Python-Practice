import sqlite3
from datetime import datetime, date


DATABASE_NAME = "tasks.db"


# ============================================================
# DATABASE
# ============================================================

def connect_database():
    return sqlite3.connect(DATABASE_NAME)


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

    print("\n" + "=" * 60)
    print("                    ADD NEW TASK")
    print("=" * 60)

    title = input("Task title: ").strip()

    if not title:
        print("❌ Task title cannot be empty.")
        return

    description = input("Description: ").strip()

    print("\n1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input(
        "Choose priority: "
    ).strip()

    priority = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }.get(priority_choice, "Medium")

    due_date = input(
        "Due date (YYYY-MM-DD): "
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
# VIEW TASKS
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

    display_tasks(
        tasks,
        "ALL TASKS"
    )


# ============================================================
# DISPLAY TASKS
# ============================================================

def display_tasks(tasks, heading):

    print("\n" + "=" * 80)
    print(f"                    {heading}")
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
            input("\nEnter task ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
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

    new_title = input(
        f"Title [{task[0]}]: "
    ).strip()

    new_description = input(
        f"Description [{task[1] or 'None'}]: "
    ).strip()

    new_priority = input(
        f"Priority [{task[2]}]: "
    ).strip().capitalize()

    new_due_date = input(
        f"Due Date [{task[3] or 'None'}]: "
    ).strip()

    if not new_title:
        new_title = task[0]

    if not new_description:
        new_description = task[1]

    if new_priority not in [
        "Low",
        "Medium",
        "High"
    ]:
        new_priority = task[2]

    if not new_due_date:

        new_due_date = task[3]

    else:

        try:
            datetime.strptime(
                new_due_date,
                "%Y-%m-%d"
            )

        except ValueError:

            print("❌ Invalid date.")
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

    print("\n✅ Task updated.")


# ============================================================
# COMPLETE TASK
# ============================================================

def complete_task():

    view_tasks()

    try:
        task_id = int(
            input("\nEnter task ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    if cursor.rowcount:

        print("✅ Task completed.")

    else:

        print("❌ Task not found.")

    connection.commit()
    connection.close()


# ============================================================
# DELETE TASK
# ============================================================

def delete_task():

    view_tasks()

    try:
        task_id = int(
            input("\nEnter task ID: ")
        )

    except ValueError:

        print("❌ Invalid ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    if cursor.rowcount:

        print("🗑️ Task deleted.")

    else:

        print("❌ Task not found.")

    connection.commit()
    connection.close()


# ============================================================
# SEARCH
# ============================================================

def search_task():

    keyword = input(
        "\nSearch keyword: "
    ).strip()

    if not keyword:

        print("❌ Keyword required.")
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
            due_date,
            created_at
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

    display_tasks(
        results,
        "SEARCH RESULTS"
    )


# ============================================================
# FILTER TASKS
# ============================================================

def filter_tasks():

    print("\n" + "=" * 60)
    print("                    FILTER TASKS")
    print("=" * 60)

    print("1. Pending Tasks")
    print("2. Completed Tasks")
    print("3. High Priority")
    print("4. Medium Priority")
    print("5. Low Priority")
    print("6. Due Today")

    choice = input(
        "\nChoose filter: "
    ).strip()

    connection = connect_database()
    cursor = connection.cursor()

    if choice == "1":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE status = 'Pending'
            ORDER BY id DESC
        """)

        heading = "PENDING TASKS"

    elif choice == "2":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE status = 'Completed'
            ORDER BY id DESC
        """)

        heading = "COMPLETED TASKS"

    elif choice == "3":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE priority = 'High'
            ORDER BY id DESC
        """)

        heading = "HIGH PRIORITY TASKS"

    elif choice == "4":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE priority = 'Medium'
            ORDER BY id DESC
        """)

        heading = "MEDIUM PRIORITY TASKS"

    elif choice == "5":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE priority = 'Low'
            ORDER BY id DESC
        """)

        heading = "LOW PRIORITY TASKS"

    elif choice == "6":

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE due_date = ?
            AND status != 'Completed'
            ORDER BY id DESC
        """, (
            date.today().isoformat(),
        ))

        heading = "TASKS DUE TODAY"

    else:

        print("❌ Invalid filter.")

        connection.close()

        return

    tasks = cursor.fetchall()

    connection.close()

    display_tasks(
        tasks,
        heading
    )


# ============================================================
# STATISTICS
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

    connection.close()

    rate = (
        completed / total * 100
        if total
        else 0
    )

    print("\n" + "=" * 65)
    print("                     TASK STATISTICS")
    print("=" * 65)

    print(f"📋 Total Tasks     : {total}")
    print(f"✅ Completed       : {completed}")
    print(f"⏳ Pending         : {pending}")
    print(f"🔴 High Priority   : {high}")
    print(f"📈 Completion Rate : {rate:.1f}%")

    print("=" * 65)


# ============================================================
# OVERDUE
# ============================================================

def show_overdue_tasks():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE due_date IS NOT NULL
          AND due_date < ?
          AND status != 'Completed'
        ORDER BY due_date ASC
    """, (
        date.today().isoformat(),
    ))

    tasks = cursor.fetchall()

    connection.close()

    display_tasks(
        tasks,
        "⚠️ OVERDUE TASKS"
    )


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
        WHERE due_date < ?
          AND status != 'Completed'
          AND due_date IS NOT NULL
    """, (
        date.today().isoformat(),
    ))

    overdue = cursor.fetchone()[0]

    connection.close()

    rate = (
        completed / total * 100
        if total
        else 0
    )

    print("\n" + "=" * 70)
    print("                 🚀 PRODUCTIVITY DASHBOARD")
    print("=" * 70)

    print(f"\n📋 Total Tasks       : {total}")
    print(f"⏳ Pending           : {pending}")
    print(f"✅ Completed         : {completed}")
    print(f"⚠️ Overdue           : {overdue}")
    print(f"📈 Completion Rate   : {rate:.1f}%")

    if rate >= 80:
        print("\n🔥 Excellent productivity!")

    elif rate >= 50:
        print("\n🚀 Good progress!")

    elif rate > 0:
        print("\n💪 Keep going!")

    else:
        print("\n🌱 Start completing tasks!")

    print("=" * 70)


# ============================================================
# MENU
# ============================================================

def show_menu():

    print("\n" + "=" * 75)
    print("                  🚀 SMART TASK MANAGER")
    print("=" * 75)

    print("1.  ➕ Add Task")
    print("2.  📋 View All Tasks")
    print("3.  ✅ Complete Task")
    print("4.  🗑️ Delete Task")
    print("5.  ✏️ Update Task")
    print("6.  🔎 Search Task")
    print("7.  📊 Task Statistics")
    print("8.  ⚠️ Overdue Tasks")
    print("9.  🚀 Productivity Dashboard")
    print("10. 🔍 Filter Tasks")
    print("11. 🚪 Exit")

    print("=" * 75)


# ============================================================
# MAIN
# ============================================================

def main():

    create_table()

    print("\n" + "=" * 75)
    print("             WELCOME TO SMART TASK MANAGER")
    print("=" * 75)

    while True:

        show_menu()

        choice = input(
            "\nChoose an option (1-11): "
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
            filter_tasks()

        elif choice == "11":

            print("\n👋 Goodbye!")
            break

        else:

            print(
                "\n❌ Invalid choice."
                "\nChoose between 1 and 11."
            )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
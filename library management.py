import json
import os
from datetime import datetime
class DataManager:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {"books": [], "members": [], "issued_books": []}
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {"books": [], "members": [], "issued_books": []}

    def save_data(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")
class BookManager:
    def __init__(self, data_manager):
        self.dm = data_manager

    def add_book(self, book_id, title, author, copies):
        for book in self.dm.data["books"]:
            if book["id"] == book_id:
                print(f"Error: Book ID {book_id} already exists!")
                return

        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "total_copies": copies,
            "available_copies": copies
        }
        self.dm.data["books"].append(new_book)
        self.dm.save_data()
        print(f"✅ Book '{title}' added successfully!")

    def list_books(self):
        if not self.dm.data["books"]:
            print("\nNo books in library.")
            return
        print("\n--- 📚 Library Inventory ---")
        print(f"{'ID':<5} {'Title':<20} {'Author':<15} {'Avail':<5}")
        print("-" * 50)
        for b in self.dm.data["books"]:
            print(f"{b['id']:<5} {b['title']:<20} {b['author']:<15} {b['available_copies']}/{b['total_copies']}")
        print("-" * 50)
class TransactionManager:
    def __init__(self, data_manager):
        self.dm = data_manager

    def issue_book(self, book_id, member_name):
        book_found = None
        for b in self.dm.data["books"]:
            if b["id"] == book_id:
                book_found = b
                break
        
        if not book_found:
            print("❌ Book not found.")
            return

        if book_found["available_copies"] <= 0:
            print("❌ Error: All copies of this book are currently issued.")
            return
        book_found["available_copies"] -= 1
        issue_record = {
            "book_id": book_id,
            "book_title": book_found["title"],
            "member_name": member_name,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.dm.data["issued_books"].append(issue_record)
        self.dm.save_data()
        print(f"✅ Book '{book_found['title']}' issued to {member_name}!")

    def return_book(self, book_id, member_name):
        # Find issue record
        record_to_remove = None
        for record in self.dm.data["issued_books"]:
            if record["book_id"] == book_id and record["member_name"] == member_name:
                record_to_remove = record
                break

        if record_to_remove:
            self.dm.data["issued_books"].remove(record_to_remove)
            # Increase availability
            for b in self.dm.data["books"]:
                if b["id"] == book_id:
                    b["available_copies"] += 1
                    break
            self.dm.save_data()
            print(f"✅ Book returned successfully.")
        else:
            print("❌ No matching issue record found.")

    def admin_view_issued(self):
        if not self.dm.data["issued_books"]:
            print("No books are currently issued.")
            return
        print("\n--- 🔐 Issued Books Report (Admin) ---")
        print(f"{'Book':<20} {'Member':<15} {'Date':<10}")
        print("-" * 50)
        for r in self.dm.data["issued_books"]:
            print(f"{r['book_title']:<20} {r['member_name']:<15} {r['date']:<10}")
        print("-" * 50)
def main():
    dm = DataManager()
    books = BookManager(dm)
    trans = TransactionManager(dm)

    while True:
        print("\n=== 📚 LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued List (Admin Only)")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            try:
                bid = int(input("Enter Book ID: "))
                title = input("Enter Title: ")
                auth = input("Enter Author: ")
                copies = int(input("Enter Total Copies: "))
                books.add_book(bid, title, auth, copies)
            except ValueError:
                print("Invalid input.")

        elif choice == '2':
            books.list_books()

        elif choice == '3':
            try:
                bid = int(input("Enter Book ID: "))
                name = input("Enter Member Name: ")
                trans.issue_book(bid, name)
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            try:
                bid = int(input("Enter Book ID: "))
                name = input("Enter Member Name: ")
                trans.return_book(bid, name)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            pwd = input("Enter Admin Password: ")
            if pwd == "6969":
                trans.admin_view_issued()
            else:
                print(" Access Denied.")

        elif choice == '6':
            exit()

if __name__ == "__main__":
    main()

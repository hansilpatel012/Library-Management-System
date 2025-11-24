# Library Management System
   A comprehensive, Python-based desktop application designed to digitize the core operations of a library. This system manages book inventories, member interactions, and the borrowing lifecycle using a              lightweight, file-based storage approach. By utilizing JSON for data persistence, the application eliminates the need for complex database servers, offering a portable and efficient solution for small to   
   medium-sized libraries.
## Key Features
   •	Smart Inventory Management: Allows librarians to add books with detailed metadata (Title, Author, ID). The system tracks "Total Copies" vs. "Available Copies" automatically to prevent issuing books that are out of stock.
   •	Secure Admin Dashboard: Includes a password-protected administrative view (Password: 3939) that allows authorized staff to view a complete report of all currently issued books and the members holding them.
   •	Intelligent Issue/Return Logic: The system validates every transaction. It prevents issuing a book if copies are unavailable and automatically updates the inventory count the moment a book is returned.
   •	Member Activity Tracking: Keeps a record of which member has borrowed which book and the date of issuance, ensuring accountability and easy tracking of overdue items.
   •	Zero-Config Data Persistence: Data integrity is maintained through a local library_data.json file. The system serializes all objects to JSON, ensuring records remain intact even after the application is         closed.
## Technologies & Design Rationale
   •	Language: Python 3.x - Selected for its readability and robust standard library.
   •	Storage Strategy: JSON - Chosen for maximum portability and zero-installation requirements.
   •	User Interface: CLI (Command Line Interface) - Ensures the application is fast, lightweight, and runs on any standard terminal.
## Modular Project Structure
   The codebase adheres to the Single Responsibility Principle:
   •	DataManager: Handles safe loading and saving of the JSON file.
   •	BookManager: Manages the library catalog and inventory logic.
   •	TransactionManager: Handles the logic for issuing and returning books, as well as the Admin report.
## Steps to Install & Run
  1.	Clone the Repository:
  2.	Navigate to Directory:
  3.	cd library-management-system
  4.	Run the Application:
  5.	python library_main.py
## Instructions for Testing
  To verify the system's robustness, perform the following test scenarios:
### Scenario A: The Happy Path (Issue & Return)
  1.	Add a Book: Select option 1. Add Book ID 101, Title "Python Basics", Author "John Doe", Copies 5.
  2.	Issue Book: Select option 3. Enter Book ID 101 and Member Name "Alice".
  3.	Verify Inventory: Select option 2. Verify that "Python Basics" now shows 4/5 available.
  4.	Return Book: Select option 4. Enter Book ID 101 and Member Name "Alice". Availability should return to 5/5.
### Scenario B: Admin Access Test
  1.	Issue a Book: Issue a book to a member.
  2.	Select Admin View: Choose option 5 from the main menu.
  3.	Enter Password: Type 6969 when prompted.
  4.	Verify Output: Ensure the transaction you just created is listed in the report.
### Scenario C: Out of Stock Prevention
  1.	Create Low Stock: Add a book with only 1 copy.
  2.	Issue Once: Issue it to "User A".
  3.	Attempt Second Issue: Try to issue the same book to "User B"
  4.	Expected Result: The system should display an error message stating the book is out of stock.



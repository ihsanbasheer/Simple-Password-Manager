Simple Password Manager with Python and PyQt

Overview:
This is a simple password manager application developed using Python and PyQt for the graphical user interface (GUI). The application connects to a local SQL database using SQLite3, providing functionalities such as adding, removing, and updating passwords. The GUI is designed with minimal styling for a clean and straightforward user experience.

Key Features:

Graphical User Interface (GUI): The application features a user-friendly GUI created with PyQt, offering an intuitive and easy-to-navigate interface.

Local SQL Database: Utilizing SQLite3, the password manager securely stores and manages passwords in a local SQL database. This ensures data persistence and retrieval for users.



Password Management:

Login page: A simple login page requesting username and password to acces the password manager.(check usage to see setting up login credentials)
Add Passwords: Users can easily add new passwords to the manager, providing details such as the website, username, and password.
Remove Passwords: Passwords that are no longer needed can be removed from the database, enhancing data management.
Update Functionality: Users have the ability to update existing passwords, allowing them to modify credentials as needed.


Implementation Technologies:

Programming Language: Python
GUI Library: PyQt (PyQt5)
Database Management System: SQLite3

Usage:

Launch Application: Run the Python script to launch the password manager application.
Login page: A login page requesting username and password (login credentials can be set in the .env file)
Add Passwords: Easily add new passwords by providing necessary details.
Remove Passwords: Delete passwords that are no longer required.
Update Credentials: Modify existing passwords when needed.
Storage: Passwords are  stored in a local SQLite database, ensuring data integrity.

Notes:

This application is designed to be a simple and lightweight password manager.
Users are encouraged to manage passwords responsibly and follow best practices for online security.
This password manager has no password hashing or other security features





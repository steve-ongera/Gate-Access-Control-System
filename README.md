# Gate Access Control System

## Overview

This is a desktop application for managing gate access control, featuring a secure login system and an admin panel for user management. The application allows administrators to add, update, and delete user accounts with sound feedback for access attempts.

## Features

- **Secure Authentication**
  - Username and password-based access control
  - Sound feedback for access granted or denied
  - Prevention of login with empty credentials

- **Admin Management Panel**
  - Add new users
  - Update existing user credentials
  - Delete user accounts
  - Real-time user list display
  - Audible notifications for successful operations

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7+
- Tkinter (usually comes pre-installed with Python)
- Pygame
- SQLite3 (included in Python standard library)

## Required Dependencies

Install the required Python libraries using pip:

```bash
pip install pygame
```

## Sound Files

The application uses the following sound files:
- `access_granted.mp3`: Played when login is successful
- `access_denied.mp3`: Played when login fails
- `user-successfully-added.mp3`: Played when a new user is added
- `delete-successful.mp3`: Played when a user is deleted
- `update-successful.mp3`: Played when user details are updated

Ensure these sound files are in the same directory as the script.

## Database Setup

The application uses an SQLite database named `tenants.db`. Before first run, create the database with the following schema:

```sql
CREATE TABLE tenants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
```

## Running the Application

1. Clone the repository
2. Install dependencies
3. Set up the database
4. Run the script:

```bash
python gate_access_control.py
```

## Application Workflow

1. **Login Screen**
   - Enter username and password
   - Click "Login"
   - Sound plays based on authentication result
     - Success: Access granted, admin panel opens
     - Failure: Access denied, error message displayed

2. **Admin Panel**
   - View existing users
   - Add new users with credentials
   - Update user credentials
   - Delete user accounts

## Security Considerations

- Passwords are stored in plain text (not recommended for production)
- Implement password hashing for enhanced security
- Limit admin account creation and access

## Potential Improvements

- Implement password hashing
- Add password complexity requirements
- Create multi-level access control
- Implement detailed access logging
- Add more robust error handling
- Integrate with physical access control systems

## Technologies Used

- Python
- Tkinter (GUI)
- Pygame (Sound)
- SQLite (Database)

## License

[Specify your license here, e.g., MIT, GPL]

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Contact

[Steve Ongera +254112284093]
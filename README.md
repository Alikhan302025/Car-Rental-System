# Car Rental Telegram Bot

A Telegram bot for managing car rentals using Python and PostgreSQL.

The bot allows users to view available cars, rent vehicles, return rented cars, and report damage directly through Telegram. The project uses a modular structure and database integration to handle rental operations and user interaction.

---

# Features

- View available cars
- Rent a car
- Return rented cars
- View rental information
- Report car damage
- Interactive Telegram menu and buttons
- Activity logging in JSON format
- PostgreSQL database integration

---

# Technologies

- Python
- Aiogram
- PostgreSQL
- Asyncpg
- JSON
- Neon Database

---

# Project Structure

The project is divided into several modules to keep the code organized and easier to maintain.

Handlers process user messages, commands, and Telegram button interactions. They are responsible for communication between the user and the system.

Services contain the main business logic of the project, including rental operations, customer management, and activity logging.

The database module handles the PostgreSQL connection and database queries.

Models represent the main objects used in the system such as cars, customers, rentals, and damage reports.

The keyboards module contains Telegram menus and buttons used for navigation inside the bot.

Additional folders are used for tests, reports, and JSON activity logs.

---

# Database

PostgreSQL database is used to store:

- Cars
- Customers
- Rental information
- Damage reports

---

# Installation & Launch

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the bot

```bash
python bot.py
```

---

# Screenshots

## Telegram Bot Interface

<img width="1918" height="1351" alt="image" src="https://github.com/user-attachments/assets/cd02d43b-9c93-42d8-8364-d29136fd8c55" />
<img width="314" height="814" alt="image" src="https://github.com/user-attachments/assets/da896f2b-f2a6-486e-bda3-da8fe28edc9f" />

---

# Team Members & Contributions

## Zhambayev Alikhan
- Created project architecture
- Designed and connected PostgreSQL database
- Implemented core Telegram bot functionality
- Developed rental system logic

## Omar Sanzhar
- Implemented Telegram buttons and menus
- Added additional functionality
- Improved user interaction and formatting

## Sabyr Rakhym
- Assisted during development
- Helped with debugging and testing
- Supported overall implementation

---

# Project Demonstrates

- Telegram bot development
- PostgreSQL integration
- OOP principles
- Exception handling
- Modular programming
- JSON file processing
- Team collaboration

---

# Conclusion

Car Rental Telegram Bot is a simple rental management system built with Python and PostgreSQL.

The project helped improve practical skills in backend development, database management, modular programming, teamwork, and Telegram bot development.

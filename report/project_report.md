# Project Report  
## KazAvtoRental Telegram Bot

### Problem Statement

Many small car rental services still manage rentals manually through messages or phone calls. This makes the process slower and less organized. The goal of this project was to create a simple Telegram bot that automates the basic car rental process and allows users to interact with the system directly inside Telegram.

---

### Solution Overview

KazAvtoRental is a Telegram bot developed using Python, aiogram, and PostgreSQL. The bot allows users to:

- view available cars
- rent a car
- return rented cars
- check rental information
- report car damage

The project uses a modular structure where different parts of the system are separated into handlers, services, database logic, and models. PostgreSQL database is hosted on Neon cloud database service.

The bot also stores activity logs in JSON format.

---

### System Design

The bot starts from the main file and processes user requests through Telegram handlers. Handlers receive commands and button interactions from users.

The main business logic is separated into service modules. These services work with rentals, customers, cars, and activity logs.

The database module connects the project with PostgreSQL and executes SQL queries for storing and retrieving data.

The project also uses OOP concepts with classes representing cars, customers, rentals, and damage reports.

---

### Challenges Faced

One of the biggest challenges during development was configuring and connecting the PostgreSQL database through Neon cloud service. Additional difficulties appeared while working with asynchronous functions in aiogram and protecting the Telegram bot token from being exposed publicly on GitHub.

The team also faced issues with database queries, user input handling, and organizing the project structure into separate modules.

---
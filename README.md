# SOLA Library Management System

## Overview

SOLA is a console-based Library Management System developed using Python and Object-Oriented Programming concepts.

The system allows:
- Borrowers to search, borrow, and return library items
- Administrators to manage library items and borrowers

This project demonstrates the use of:
- Binary Search Tree (BST)
- Doubly Linked List
- Inheritance and Polymorphism
- Modular Programming
- Role-based Login System

---

## Features

### Borrower Functions
- Login authentication
- Search items by:
  - title
  - author
  - category
  - language
  - year
- Borrow items
- Return items
- View borrowed items
- Check fines
- Pay fines

### Administrator Functions
- Login authentication
- Display all library items
- Add new items
- Search borrowers
- Display all borrowers
- Update borrower details
- Remove borrowers

---

## Data Structures Used

### Binary Search Tree (BST)
Used to store library items for faster searching operations.

### Doubly Linked List
Used to manage borrowers efficiently for:
- insertion
- deletion
- traversal
- updating

---

## Project Structure

```text
SOLA/
│
├── models/
├── services/
├── data_structures/
├── generate_data/
├── menus/
├── utils/
└── main.py


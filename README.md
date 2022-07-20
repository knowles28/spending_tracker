# spending_tracker

# Overview

## **Spending Tracker Project**

This was my first solo project at CodeClan. The task was to create a full stack app in 7 days using HTML/CSS, Python, Flask and PostgreSQL.

---

# Brief

### **Spending Tracker**

Build an app that allows a user to track their spending, highlighting the most common type of transactions they make

### **MVP**

- A dashboard that displays all the transactions a user has made in a single view
    - showing each transaction description, amount, merchant, tag
    - showing total for all transactions
- The user can add new transactions with the following information: description, price,  tags and merchants.
- The app should allow the user to create and edit merchants
- The app should allow the user to create and edit tags

### **Inspired by:**

- Starling, Monzo (mobile banking apps)

### **Extensions**

- Show transaction target amount
- add images for merchants/tags
- The user should be able to assign *Merchants* and *Tags* as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
- Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
- The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
- The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

---

# HOW TO RUN

*Instructions for Apple Terminal*

- Clone the project:
    - *git clone [https://github.com/knowles28/spending_tracker](https://github.com/knowles28/spending_tracker)*
- Create the database:
    - *createdb spending_tracker*
    - *psql -d spending_tracker -f spending_tracker.sql*
- Run the file and populate examples:
    - *python3 console.py*
- Open the client view from local host:
    - flask run

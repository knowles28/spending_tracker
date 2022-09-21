# Spendless: Education App
This was my first solo project at CodeClan. The task was to create a full stack app in 7 days using HTML/CSS, Python, Flask and PostgreSQL. We we not allowed to use Javascript for the project.


### Contents 

* [Example coming soon!]
* [Technologies](#technologies)
* [Brief](#brief)
* [Challenges](#challenges)
* [Installation](#installation)

<br>



## Technologies

These are the main technologies I used to contruct the project:

* ![Python]
* ![Flask]
* ![PostGres]
* ![HTML]
* ![css]

<br>


## Brief

**Spending Tracker**

Build an app that allows a user to track their spending, highlighting the most common type of transactions they make in their daily life.

**MVP**

- A dashboard that displays all the transactions a user has made in a single view
    - showing each transaction description, amount, merchant, tag
    - showing total for all transactions
- The user can add new transactions with the following information: description, price,  tags and merchants.
- The app should allow the user to create and edit merchants
- The app should allow the user to create and edit tags

**Inspired by:**

- Starling, Monzo (mobile banking apps)

**Extensions**

- [x] The user should be able to assign *Merchants* and *Tags* as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
- [x] Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
- [x] The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
- [ ] add images for merchants/tags
- [x] The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.


<br>


## Challenges

Here are some of the key learning points from my first solo project:

* Filtering using URL parameters.
* Using TDD effectively.
* Bug tracking.
* Planning REStful route.

<br>


## Installation

*Instructions for Apple Terminal*

- Clone the project:

```git clone [https://github.com/knowles28/spending_tracker](https://github.com/knowles28/spending_tracker)```

- Create the database:

```createdb spending_tracker```

```psql -d spending_tracker -f spending_tracker.sql```

- Run the file and populate examples:

```python3 console.py```

- Open the client view from local host:

```flask run```




<!-- MARKDOWN LINKS & IMAGES -->

[Python]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Flask]:https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[PostGres]:https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[HTML]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[css]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white



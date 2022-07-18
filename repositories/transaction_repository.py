from db.run_sql import run_sql

from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = """
    INSERT INTO transactions(merchant_id, description, tag_id, price, date) VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    values = [transaction.merchant, transaction.description, transaction.tag, transaction.price, transaction.date]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(merchant, row['description'], tag, row['price'], row['date'], row['id'])
        transactions.append(transaction)
    
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]

        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        
        transaction = Transaction(merchant, result['description'], tag, result['price'], result['date'], result['id'])
    return transaction

        

def update(transaction):
    
    sql = "UPDATE transactions SET (merchant_id, description, tag_id, price, date) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant, transaction.description, transaction.tag, transaction.price, transaction.date, transaction.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def total():
    total = 0
    all_transactions = select_all()
    
    for row in all_transactions:
        total += row.price
    
    return total
      







# ______________SQL DUMP____________


    # SELECT transactions.*, merchants.merchant_name, tags.tag_name
    # FROM transactions
    # INNER JOIN merchants 
    #     ON transactions.merchant_id = merchants.id
    # INNER JOIN tags 
    #     ON transactions.tag_id = tags.id



# SELECT name FROM merchants
# FROM merchants
# INNER JOIN transactions.description
# 	ON transactions.merchant_id = merchants.id
# WHERE transactions.merchant_id = merchants.id

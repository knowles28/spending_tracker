from db.run_sql import run_sql

from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = """
    INSERT INTO transactions(merchant, description, tag, price) VALUES (%s, %s, %s, %s) RETURNING *
    """
    values = [transaction.merchant, transaction.description, transaction.tag, transaction.price]
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
        transaction = Transaction(merchant, row['description'], tag, row['price'])
        transactions.append(transaction)
    
    return transactions













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

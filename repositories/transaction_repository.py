from db.run_sql import run_sql

from models.transaction import Transaction


def save(transaction):
    sql = """
    
    INSERT INTO transactions(merchant_id, description, tag_id, price) VALUES (%s, %s, %s, %s) RETURNING *
    """
    values = [transaction.merchant_id, transaction.description, transaction.tag_id, transaction.price]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():
    transactions = []
    sql = """
    SELECT transactions.*, merchants.merchant_name, tags.tag_name
    FROM transactions
    INNER JOIN merchants 
        ON transactions.merchant_id = merchants.id
    INNER JOIN tags 
        ON transactions.tag_id = tags.id

    """
    results = run_sql(sql)
    
    for row in results:
        transaction = Transaction(row['merchant_id'], row['description'], row['tag_id'], row['price'])
        transactions.append(transaction)
    
    return transactions


# # MERCHANTS
# def merchant(transaction):
#     merchant = None
    
#     sql = """
#     SELECT name FROM merchants
#     FROM merchants
    
#     """

# # TAGS










# SELECT name FROM merchants
# FROM merchants
# INNER JOIN transactions.description
# 	ON transactions.merchant_id = merchants.id
# WHERE transactions.merchant_id = merchants.id

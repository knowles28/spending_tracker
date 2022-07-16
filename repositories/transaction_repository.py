from db.run_sql import run_sql

from models.transaction import Transaction


def save(transaction):
    sql = """
    
    INSERT INTO transactions(merchant_id, description, tag_id, _date, price) VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    values = [transaction.merchant_id, transaction.description, transaction.tag_id, transaction._date, transaction.price]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    
    for row in results:
        transaction = Transaction( row['id'], row['merchant_id'], row['description'], row['tag_id'], row['_date'], row['price'])
        transactions.append(transaction)
    
    return transactions


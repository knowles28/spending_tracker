from db.run_sql import run_sql

from models.transaction import Transaction


def save(transaction):
    sql = "INSERT INTO transactions (merchant, description, tag, date, price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.description]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    
    for row in results:
        transaction = transaction(row['merchant'], row['description'], row['tag'], row['date'], row['price'], row['id'])
        transactions.append(transaction)
    
    return transactions

# def select(id):
#     transaction = None
#     sql = "SELECT * from transactions WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
    
#     # note to self - if statement without condition checks variable is not empty
#     if results:
#         result = results[0]
#         transaction = transaction(result['description'], result['id'])
    
#     return transaction
        
        

# def update(transaction):
#     sql = "UPDATE transactions SET description = %s WHERE id = %s"
#     values = [transaction.description, transaction.id]
#     run_sql(sql, values)


# def delete(id):
#     sql = "DELETE FROM transactions WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


from db.run_sql import run_sql
from models.budget import Budget



def save(budget):
    sql = "INSERT INTO budgets (amount) VALUES (%s) RETURNING *"
    values = [budget.amount]
    result = run_sql(sql, values)
    budget.id = result[0]['id']
    return budget

def select():
    budget = None
    sql = "select * from budgets ORDER BY id DESC LIMIT 1"
    results = run_sql(sql)
    if results:
        result = results[0]
        budget = Budget(result['amount'], result['id'])
    return budget
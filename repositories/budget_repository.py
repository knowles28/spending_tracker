from db.run_sql import run_sql


def save(target):
    sql = "INSERT INTO budgets (amount) VALUES  %s RETURNING *"
    values = [target.amount]
    results = run_sql(sql, values)
    target.id = results[0]['id']
    return target

def select():
    sql = "select * from budgets ORDER BY id DESC LIMIT 1"
    values = [id]
    result = run_sql(sql, values)
    
    return result
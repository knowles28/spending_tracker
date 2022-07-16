from db.run_sql import run_sql

from models.merchant import Merchant


def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * from merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    # note to self - if statement without condition checks variable is not empty
    if results:
        result = results[0]
        merchant = Merchant(result['name'], result['id'])
    
    return merchant
        
        

def update(merchant):
    sql = "UPDATE merchants SET (name) = (%s) WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


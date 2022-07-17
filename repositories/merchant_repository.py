from db.run_sql import run_sql

from models.merchant import Merchant


def save(merchant):
    sql = "INSERT INTO merchants (merchant_name) VALUES (%s) RETURNING *"
    values = [merchant.merchant_name]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    
    for row in results:
        merchant = Merchant(row['merchant_name'], row['id'])
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
        merchant = Merchant(result['merchant_name'], result['id'])
    
    return merchant
        
        

def update(merchant):
    sql = "UPDATE merchants SET merchant_name = %s WHERE id = %s"
    values = [merchant.merchant_name, merchant.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


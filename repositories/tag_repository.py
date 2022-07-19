from db.run_sql import run_sql

from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, restricted) VALUES (%s, %s) RETURNING *"
    values = [tag.name, tag.restricted]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    
    for row in results:
        tag = Tag(row['name'], row['restricted'], row['id'])
        tags.append(tag)
    
    return tags

def select(id):
    tag = None
    sql = "SELECT * from tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    # reminder note to self - if statement without condition checks variable is not empty
    if results:
        result = results[0]
        tag = Tag(result['name'], result['restricted'], result['id'])
    
    return tag
        
        

def update(tag):
    sql = "UPDATE tags SET (name, restricted) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.restricted, tag.id]
    run_sql(sql, values)
    


def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)


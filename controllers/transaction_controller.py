from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
from models.budget import Budget

import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.budget_repository as budget_repository

transactions_blueprint = Blueprint("transactions", __name__)

#ALL
@transactions_blueprint.route("/transactions")
def transactions():
    tag_filter = request.args.get('tags', default='all')
    # breakpoint()
    sort_by_filter = request.args.get('sort-by', default='newest')
    transactions = transaction_repository.select_all(tag_filter, sort_by_filter)
    total = transaction_repository.total()
    target_budget = budget_repository.select()
    tags = tag_repository.select_all()
    
    
    print(tag_filter)

    return render_template("transactions/index.html", all_transactions=transactions, total=total, target_budget=target_budget, all_tags=tags, tag_filter=tag_filter, sort_by_filter=sort_by_filter)


#EXTENSION - FILTERS W/ URL PARAMETERS
@transactions_blueprint.route("/transactions/filter", methods=['POST'])
def filters():
    tags = request.form['tags-filter']
    sortby = request.form['sort-by-filter']
    
    return redirect(f"/transactions?tags={tags}&sort-by={sortby}")
    

#NEW
@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("/transactions/new.html", all_merchants = merchants, all_tags = tags)

#CREATE
@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    merchant_id = request.form['merchant_id']
    description = request.form['description']
    tag_id      = request.form['tag_id']
    price       = request.form['price']
    date        = request.form['date']
    
    transaction = Transaction(merchant_id, description, tag_id, price, date)
    transaction_repository.save(transaction)
    
    return redirect("/transactions")

#EDIT '/transactions/<id>/edit'
@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    
    return render_template("/transactions/edit.html", transaction=transaction, all_merchants = merchants, all_tags = tags)


#UPDATE '/transactions' [POST]
@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    merchant_id = request.form['merchant_id']
    description = request.form['description']
    tag_id      = request.form['tag_id']
    price       = request.form['price']
    date        = request.form['date']

    transaction = Transaction(merchant_id, description, tag_id, price, date, id)
    transaction_repository.update(transaction)    
    return redirect("/transactions")

#DELETE '/transactions/? [POST]
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    
    return redirect("/transactions")


# EXTENSIONS ___________________________________________________


@transactions_blueprint.route("/transactions/edit-target", methods=['GET'])
def edit_target():
    return render_template("/transactions/target.html")

@transactions_blueprint.route("/transactions/update-target", methods=['POST'])
def update_target():
    updated_target = request.form['target']
    new_budget = Budget(updated_target)
    budget_repository.save(new_budget)
    return redirect("/transactions")

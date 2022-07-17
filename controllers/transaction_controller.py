from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

#ALL
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total()
    return render_template("transactions/index.html", all_transactions=transactions, total=total)

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
    
    transaction = Transaction(merchant_id, description, tag_id, price)
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

    transaction = Transaction(merchant_id, description, tag_id, price, id)
    transaction_repository.update(transaction)    
    return redirect("/transactions")


#DELETE '/transactions/? [POST]
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    
    return redirect('/transactions')

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions=transactions)

@transactions_blueprint.route("/transactions/new", methods=['POST'])
def new_transaction():
    return render_template("/transactions/new.html")
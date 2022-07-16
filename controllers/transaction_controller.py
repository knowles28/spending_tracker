from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions=transactions)


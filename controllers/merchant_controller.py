from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", all_merchants=merchants)


# NEW '/merchants/new'
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")


# CREATE '/merchants'  [POST]
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form['merchant-name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    
    return redirect("/merchants")
#

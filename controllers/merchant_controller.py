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
@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    
    return render_template("merchants/new.html")


# CREATE '/merchants'  [POST]
@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['merchant-name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    
    return redirect("/merchants")


#EDIT '/merchants/<id>/edit'
@merchants_blueprint.route("/merchants/<id>/edit", methods=['POST'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    
    return render_template("/merchants/edit.html", merchant=merchant)


#UPDATE '/merchants' [PUT/POST?]
@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['merchant-name']
    restricted = request.form['restricted']
    
    merchant = Merchant(name, restricted, id)
    
    merchant_repository.update(merchant)
    
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/update-restricted", methods=['POST'])
def restrict_tag(id):
    merchant = merchant_repository.select(id)
    
    if merchant.restricted == True:
        merchant.mark_unrestricted()
    else:
        merchant.mark_restricted()
    
    merchant_repository.update(merchant)
    
    return redirect("/merchants")


#DELETE '/merchants/edit'? [POST]
@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    
    return redirect('/merchants')

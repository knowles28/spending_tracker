from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    
    return render_template("tags/index.html", all_tags=tags)


# NEW '/tags/new'
@tags_blueprint.route("/tags/new", methods=['GET'])
def new_tag():
    return render_template("tags/new.html")


# CREATE '/tags'  [POST]
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    name = request.form['tag-name']
    tag = Tag(name)
    tag_repository.save(tag)
    
    return redirect("/tags")


#EDIT '/tags/<id>/edit'
@tags_blueprint.route("/tags/<id>/edit", methods=['POST'])
def edit_tag(id):
    tag = tag_repository.select(id)
    
    return render_template("/tags/edit.html", tag=tag)


#UPDATE '/tags' [PUT/POST?]
@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    name = request.form['tag-name']
    tag = Tag(name, id)
    
    tag_repository.update(tag)
    
    return redirect("/tags")


#DELETE '/tags/edit'? [POST]
@tags_blueprint.route("/tags/<id>/delete", methods=['POST'])
def delete_tag(id):
    tag_repository.delete(id)
    
    return redirect('/tags')

from flask import render_template, Blueprint, request

views = Blueprint("views",__name__)

#view is a blueprint

stuff = ["Some stuff","More stuff","Even more stuff","Tim's stuff"]

task_list = []

@views.route("/")
def home():
    name = "Tim"
    return render_template("index.html",name=name)

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/about")
def about():
    return render_template("about.html",content=stuff)

@views.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")

@views.route("/todos", methods=["GET","POST"])
def todo():
    if request.method == "POST":
        task = request.form.get("task-input")
        task_list.append(task)
        print(task_list)
        
    return render_template("todos.html",task_list = task_list)



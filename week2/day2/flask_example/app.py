from flask import Flask
from views import views
#import views from views.py

#instantiate app object
app = Flask(__name__)

# register the views blueprint
app.register_blueprint(views)

#run application
if __name__ == "__main__":
    app.run(debug=True,port=8000)


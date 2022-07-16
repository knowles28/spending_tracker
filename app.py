from flask import Flask, render_template

# CONTROLLER IMPORTS
from controllers.merchant_controller import merchants_blueprint
from controllers.tag_controller import tags_blueprint

app = Flask(__name__)

# REGISTER BLUEPRINTS
app.register_blueprint(merchants_blueprint)
app.register_blueprint(tags_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
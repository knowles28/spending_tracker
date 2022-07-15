from flask import Flask, render_template

# CONTROLLER IMPORTS

app = Flask(__name__)

# REGISTER BLUEPRINTS

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
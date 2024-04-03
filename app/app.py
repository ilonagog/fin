# from flask import Flask, render_templete 
# from flask_migrate import Migrate
# from models import db, Pet

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_app.db'

# # migrate = Migrate(app,db)
# db.init_app(app)

# @app.route('/')
# def index():
#     return '<h1>Hello World</h1>'

# @app.route('/pets/<int:id')
# def show_pet(id):
#     pet = Pet.query.get(id)
#     if pet:
#         return render_templete('')

from flask import Flask, render_template
from models import Pet  # Import the Pet model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_app.db'

# Define a route to display the details of a pet
@app.route('/pets/<int:id>')
def pet(id):
    # Query the database for the pet with the specified ID
    pet = Pet.query.get(id)
    if pet:
        # If the pet exists, render a template to display its details
        return render_template('pet.html', pet=pet)
    else:
        # If the pet doesn't exist, return a 404 error
        return render_template('404.html'), 404

# Define a route to handle the home page
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(debug=True)
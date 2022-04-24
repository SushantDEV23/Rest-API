from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' #Configuring the database so that we can connect to it

db=SQLAlchemy(app)   #Passing db to app


class Drinks(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True, nullable=False)
    description=db.Column(db.String(120))

    def __repr__(self):   #representation
        return f"{self.name}-{self.description}"


@app.route("/drinks")
def get_drinks():
    drink=Drinks(name="Whiskeys", description="for men")
    db.session.add(drink)
    db.session.commit()

    drinks=Drinks.query.all()

    output=[]
    for drink in drinks:
        drink_data={'name':drink.name, 'description':drink.description}
        output.append(drink_data)
    return {"drinks":output}

@app.route("/drinks/<id>")
def get_drink(id):
    drink=Drinks.query.get_or_404(id)
    return {"name":drink.name, "description":drink.description}

@app.route('/drinks', method=['POST'])
def add_drink():
    drink=Drinks(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()

    return {'id':drink.id}

@app.route('/drinks', methods=['DELETE'])
def del_drink(id):
    drink=Drinks.query.get(id)
    if drink is None:
        return {"Error": "404 Not Found"}

    db.session.delete(drink)
    db.session.commit()

    return {"message":"This was successfull"}




app.run(debug=True)
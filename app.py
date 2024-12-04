from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import stripe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Preorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    payment_method_id = db.Column(db.String(100), nullable=False)

def create_tables():
    """Function to create database tables."""
    with app.app_context():  # Create an application context
        db.create_all()

@app.route('/')
def home():
    return "Welcome to the Preorder API!"

@app.route('/preorder', methods=['POST'])
def preorder():
    data = request.get_json()
    name = data['name']
    item = data['item']
    payment_method_id = data['paymentMethodId']

    try:
        charge = stripe.Charge.create(
            amount=2500,
            currency='usd',
            payment_method=payment_method_id,
            confirmation_method='manual',
            confirm=True
        )

        new_preorder = Preorder(name=name, item=item, payment_method_id=payment_method_id)
        db.session.add(new_preorder)
        db.session.commit()

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/preorders', methods=['GET'])
def get_preorders():
    preorders = Preorder.query.all()
    return jsonify([{ 'name': p.name, 'item': p.item } for p in preorders]), 200

if __name__ == '__main__':
    create_tables()  # Call table creation function
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
import stripe

app = Flask(__name__)
CORS(app)  # This will allow all origins by default

# Set your Stripe secret key
stripe.api_key = 'sk_test_51Pird5GW5HJ0bhAn0kFQr2HGla0Yxr7hfOxCsUULZzj7UY8t3lkWa5fd5Y9f0IZ3gYctUMx2heMTTbGZ8LWhTbPF00xrQqbDvw'

@app.route('/api/create-checkout-session', methods=['POST'])
def create_checkout_session():
    print("Hello")
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'api/success',
            cancel_url=request.host_url + 'api/cancel',
        )
        return jsonify({'id': session.id})
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 403

@app.route('/api/success', methods=['GET'])
def success():
    return jsonify({'message': 'Payment succeeded!'})

@app.route('/api/cancel', methods=['GET'])
def cancel():
    return jsonify({'message': 'Payment canceled.'})

if __name__ == '__main__':
    app.run(port=4242)
import React from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('pk_test_51Pird5GW5HJ0bhAndQ3eqjsaNjd2S2EQHFyi5279XgeLTfi27rMzKsZcmQe4vWwUiV8i4bZsVNhrsqge0jrQTv3f00FwJoor3R'); // Replace with your public key

const App = () => {
  const handleCheckout = async () => {
    const response = await fetch('http://127.0.0.1:4242/api/create-checkout-session', {
      method: 'POST',
    });
    const sessionId = (await response.json()).id;
    const stripe = await stripePromise;
    await stripe.redirectToCheckout({ sessionId });
  };

  return (
    <div>
      <h1>Buy a T-shirt</h1>
      <button role="link" onClick={handleCheckout}>
        Checkout
      </button>
    </div>
  );
};

export default App;
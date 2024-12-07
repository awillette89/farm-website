require('dotenv').config(); // Load environment variables

const stripe = Stripe(process.env.STRIPE_PUBLIC_KEY); // Use the environment variable for the public key

const appearance = { /* appearance */ };
const options = {
  layout: {
    type: 'tabs',
    defaultCollapsed: false,
  }
};

const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');
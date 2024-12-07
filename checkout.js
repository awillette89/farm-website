import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe(process.env.STRIPE_PUBLIC_KEY);

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
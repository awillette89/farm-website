const stripe = Stripe('pk_test_51QS0tQGMpgCaGok4YWtuf7yRAggwkWtxYDRUKpjTsh3smR0RxxzU1QSYyjdljCsklqzl8AbsYY5anKAc11XQS3lS00mUTR7Z6w');

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
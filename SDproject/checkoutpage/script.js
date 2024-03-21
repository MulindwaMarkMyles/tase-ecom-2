document.getElementById('checkout-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var address = document.getElementById('address').value;
    var cardNumber = document.getElementById('card-number').value;
    var expiryDate = document.getElementById('expiry-date').value;
    var cvv = document.getElementById('cvv').value;

    // Basic form validation
    if (name === '' || email === '' || address === '' || cardNumber === '' || expiryDate === '' || cvv === '') {
        alert('Please fill in all fields.');
        return;
    }

    

    alert('Form submitted successfully!');
});

// After form submission
var checkoutForm = document.getElementById('checkout-form');
checkoutForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    
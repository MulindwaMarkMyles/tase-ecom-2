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
    
    // Fetch form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var address = document.getElementById('address').value;
    var paymentMethod = document.getElementById('payment-method').value;
    
    // You can perform further actions here, like sending data to a server
    
    // For demonstration, let's just log the data
    console.log("Name: " + name);
    console.log("Email: " + email);
    console.log("Address: " + address);
    console.log("Payment Method: " + paymentMethod);

    // Redirect to order status page
    window.location.href = 'order_status.html';
});

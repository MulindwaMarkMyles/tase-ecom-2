// Simulated data
const totalSales = 5000;
const pendingOrders = 10;
const dailyOrders = 20;
const profits = 3000;

// Update DOM with data
document.querySelector('.total-sales p').textContent = '$' + totalSales;
document.querySelector('.pending-orders p').textContent = pendingOrders;
document.querySelector('.daily-orders p').textContent = dailyOrders;
document.querySelector('.profits p').textContent = '$' + profits;

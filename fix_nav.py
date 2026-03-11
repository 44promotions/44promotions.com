with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Track Order - should go to track-order.html
content = content.replace(
    "function trackOrder() {\n    const orderId = prompt('Please enter your order number:');\n    if (orderId) {\n        alert('Order tracking for: ' + orderId + '\\n\\nThis feature is coming soon!');\n    }\n}",
    "function trackOrder() {\n    window.location.href = 'track-order.html';\n}"
)

# Remove duplicate function definitions (keep only the last ones)
# First, remove the early duplicates
content = content.replace(
    '''

// Button Functions
function toggleCategories() {
    alert('Categories dropdown - use category cards below to filter');
}

function filterByCategory(category) {
    window.location.href = 'products.html?category=' + encodeURIComponent(category);
}

function viewProduct(id) {
    window.location.href = 'product-detail.html?id=' + id;
}

function goHome() {
    window.location.href = 'index.html';
}

function goProducts() {
    window.location.href = 'products.html';
}

function trackOrder() {
    const orderId = prompt('Please enter your order number:');
    if (orderId) {
        alert('Order tracking for: ' + orderId + '\\n\\nThis feature is coming soon!');
    }
}

function contactUs() {
    window.location.href = 'mailto:info@44promotions.com?subject=Contact Us';
}

function searchProducts() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        window.location.href = 'products.html?search=' + encodeURIComponent(query);
    }
}

function signIn() {
    alert('Sign In\\n\\nThis feature is coming soon!');
}

function register() {
    alert('Register\\n\\nThis feature is coming soon!');
}

function addToCart() {
    alert('Add to Cart\\n\\nThis feature is coming soon!');
}

function goToWishlist() {
    alert('Wishlist\\n\\nThis feature is coming soon!');
}

// Update header buttons
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchProducts();
    }
});''',
    ''
)

# Fix remaining old functions
content = content.replace(
    "function signIn() {\n    alert('Sign In\\\\n\\\\nThis feature is coming soon!');}",
    "function signIn() {\n    window.location.href = 'login.html';}"
)

content = content.replace(
    "function register() {\n    alert('Register\\\\n\\\\nThis feature is coming soon!');}",
    "function register() {\n    window.location.href = 'register.html';}"
)

content = content.replace(
    "function addToCart() {\n    alert('Add to Cart\\\\n\\\\nThis feature is coming soon!');}",
    "function addToCart() {\n    window.location.href = 'cart.html';}"
)

content = content.replace(
    "function goToWishlist() {\n    alert('Wishlist\\\\n\\\\nThis feature is coming soon!');}",
    "function goToWishlist() {\n    window.location.href = 'wishlist.html';}"
)

with open(r'D:\Openclaw-Local\44promotions.com\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed index.html navigation!')

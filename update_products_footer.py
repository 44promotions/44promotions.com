with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Improve pagination - show more pages with Prev/Next
old_pagination = '''function renderPagination() {
  const totalPages = Math.ceil(filtered.length / perPage);
  const pag = document.getElementById('pagination');
  let html = '';
  
  for (let i = 1; i <= Math.min(totalPages, 5); i++) {
    html += `<a href="#" class="${i === currentPage ? 'active' : ''}" onclick="goToPage(${i})">${i}</a>`;
  }
  
  if (totalPages > 5) {
    html += `<span>...</span><a href="#" onclick="goToPage(${totalPages})">${totalPages}</a>`;
  }
  
  pag.innerHTML = html;
}'''

new_pagination = '''function renderPagination() {
  const totalPages = Math.ceil(filtered.length / perPage);
  const pag = document.getElementById('pagination');
  let html = '';
  
  // Previous button
  if (currentPage > 1) {
    html += `<a href="#" onclick="goToPage(${currentPage - 1})">Prev</a>`;
  }
  
  // Page numbers
  const start = Math.max(1, currentPage - 2);
  const end = Math.min(totalPages, currentPage + 2);
  
  for (let i = start; i <= end; i++) {
    html += `<a href="#" class="${i === currentPage ? 'active' : ''}" onclick="goToPage(${i})">${i}</a>`;
  }
  
  // Next button
  if (currentPage < totalPages) {
    html += `<a href="#" onclick="goToPage(${currentPage + 1})">Next</a>`;
  }
  
  pag.innerHTML = html;
}'''

content = content.replace(old_pagination, new_pagination)

# Add footer to products.html (before </body>)
footer = '''

<!-- Footer -->
<footer style="background: #1a1a1a; color: #fff; padding: 40px 0; margin-top: 60px;">
  <div class="container">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px;">
      <div>
        <h5 style="color: #f4c542; margin-bottom: 15px; text-transform: uppercase; font-size: 14px;">Quick Links</h5>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 10px;"><a href="#" onclick="goHome()" style="color: #aaa; text-decoration: none;">Home</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="goProducts()" style="color: #aaa; text-decoration: none;">Products</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="alert(\'About Us\\n\\nComing soon!\')" style="color: #aaa; text-decoration: none;">About Us</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="contactUs()" style="color: #aaa; text-decoration: none;">Contact</a></li>
        </ul>
      </div>
      <div>
        <h5 style="color: #f4c542; margin-bottom: 15px; text-transform: uppercase; font-size: 14px;">Categories</h5>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 10px;"><a href="products.html?category=Bags+%26+Travel" style="color: #aaa; text-decoration: none;">Bags & Travel</a></li>
          <li style="margin-bottom: 10px;"><a href="products.html?category=Drinkware" style="color: #aaa; text-decoration: none;">Drinkware</a></li>
          <li style="margin-bottom: 10px;"><a href="products.html?category=Office" style="color: #aaa; text-decoration: none;">Office</a></li>
          <li style="margin-bottom: 10px;"><a href="products.html?category=Tech" style="color: #aaa; text-decoration: none;">Tech</a></li>
        </ul>
      </div>
      <div>
        <h5 style="color: #f4c542; margin-bottom: 15px; text-transform: uppercase; font-size: 14px;">Support</h5>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 10px;"><a href="#" onclick="trackOrder()" style="color: #aaa; text-decoration: none;">Track Order</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="alert(\'FAQ\\n\\nComing soon!\')" style="color: #aaa; text-decoration: none;">FAQ</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="alert(\'Shipping Info\\n\\nComing soon!\')" style="color: #aaa; text-decoration: none;">Shipping Info</a></li>
          <li style="margin-bottom: 10px;"><a href="#" onclick="alert(\'Returns\\n\\nComing soon!\')" style="color: #aaa; text-decoration: none;">Returns</a></li>
        </ul>
      </div>
      <div>
        <h5 style="color: #f4c542; margin-bottom: 15px; text-transform: uppercase; font-size: 14px;">Contact</h5>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 10px;"><a href="mailto:info@44promotions.com" style="color: #aaa; text-decoration: none;"><i class="fas fa-envelope"></i> info@44promotions.com</a></li>
          <li style="margin-bottom: 10px;"><a href="tel:+1234567890" style="color: #aaa; text-decoration: none;"><i class="fas fa-phone"></i> +1 (234) 567-890</a></li>
          <li style="margin-bottom: 10px;"><span style="color: #aaa;"><i class="fas fa-map-marker-alt"></i> USA</span></li>
        </ul>
      </div>
    </div>
    <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #333; color: #666; font-size: 12px;">
      &copy; 2026 44Promotions. All rights reserved.
    </div>
  </div>
</footer>
'''

# Add footer before </body>
content = content.replace('</body>', footer + '</body>')

with open(r'D:\Openclaw-Local\44promotions.com\products.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('products.html updated with improved pagination and footer!')

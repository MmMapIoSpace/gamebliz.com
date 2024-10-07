import json
from datetime import datetime, timedelta

def generate_products(num_products):
    products = []
    base_time = datetime.utcnow()

    for i in range(1, num_products + 1):
        product = {
            "Id": i,
            "Timestamp": (base_time + timedelta(minutes=i * 5)).isoformat() + "Z",
            "Name": f"Product {i}",
            "Price": round(50 + i * 2.5, 2),  # Menghasilkan harga produk yang berbeda
            "Picture": f"https://picsum.photos/200/300?random={i}"  # URL gambar placeholder dari Lorem Picsum
        }
        products.append(product)
    return products

def save_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

num_products = 40  # Jumlah produk yang ingin dihasilkan
products = generate_products(num_products)
save_to_json('product.json', products)

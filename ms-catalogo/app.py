# catalogo/app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Simulamos una base de datos de productos
PRODUCTS = {
    1: {"name": "Laptop", "price": 1000, "stock": 10},
    2: {"name": "Smartphone", "price": 500, "stock": 20},
}

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

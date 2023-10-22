# Django Product API

This is a Django project that provides a RESTful API for managing products. You can create, retrieve, update, and delete products using HTTP requests. 

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher

## Installation

1. Clone this repository: `git clone https://github.com/ianuragg/django-product-api.git`
2. Create and activate a virtual environment: `python -m venv env && source env/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run the migrations: `python manage.py migrate`
5. Run the server: `python manage.py runserver`

## Note

This project includes two versions of views: function based views and class based views. You can use either version according to your preference by uncommenting the corresponding code in the `views.py` file.


## Usage

You can use any HTTP client to interact with the API endpoints. Here are some examples using curl:

- To get a list of all products: `curl http://localhost:8000/products/`
- To get a single product by id: `curl http://localhost:8000/products/1/`
- To create a new product: `curl -X POST -H "Content-Type: application/json" -d '{"name": "New Product", "price": 9.99, "category": "New Category", "description": "New Description"}' http://localhost:8000/products/`
- To update an existing product: `curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Product", "price": 19.99, "category": "Updated Category", "description": "Updated Description"}' http://localhost:8000/products/1/`
- To delete an existing product: `curl -X DELETE http://localhost:8000/products/1/`

## Features

- CRUD operations for products
- Pagination for product list
- Search and filter for product list

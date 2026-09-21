from fastapi import FastAPI

app = FastAPI()

# Restaurant menu
Menu = [
    {
        "name": "Spring Rolls",
        "price": 5.99,
        "category": "appetizer",
        "is_vegetarian": True
    },
    {
        "name": "Chicken Wings",
        "price": 8.99,
        "category": "appetizer",
        "is_vegetarian": False
    },
    {
        "name": "Garlic Bread",
        "price": 4.99,
        "category": "appetizer",
        "is_vegetarian": True
    },
    {
        "name": "Calamari",
        "price": 9.99,
        "category": "appetizer",
        "is_vegetarian": False
    },

    {
        "name": "Grilled Chicken",
        "price": 15.99,
        "category": "main",
        "is_vegetarian": False
    },
    {
        "name": "Beef Steak",
        "price": 22.99,
        "category": "main",
        "is_vegetarian": False
    },
    {
        "name": "Vegetable Pasta",
        "price": 13.99,
        "category": "main",
        "is_vegetarian": True
    },
    {
        "name": "Fish and Chips",
        "price": 17.99,
        "category": "main",
        "is_vegetarian": False
    },
    {
        "name": "Mushroom Risotto",
        "price": 16.99,
        "category": "main",
        "is_vegetarian": True
    },

    {
        "name": "Chocolate Cake",
        "price": 7.99,
        "category": "dessert",
        "is_vegetarian": True
    },
    {
        "name": "Cheesecake",
        "price": 8.99,
        "category": "dessert",
        "is_vegetarian": True
    },
    {
        "name": "Ice Cream",
        "price": 5.99,
        "category": "dessert",
        "is_vegetarian": True
    }
]


# 1. GET /menu
@app.get("/menu")
def get_menu():
    return{"message": "Welcome to our restaurant!"}
    


# 2. GET /appetizers
@app.get("/appetizers")
def get_appetizers():
    return [
        item["name"]
        for item in menu
        if item["category"] == "appetizer"
    ]

# 3. GET /main-courses
@app.get("/main-courses")
def get_main_courses():
    return [
        item["name"]
        for item in menu
        if item["category"] == "main"
    ]

# 4. GET /desserts
@app.get("/desserts")
def get_desserts():
    return [
        item["name"]
        for item in menu
        if item["category"] == "dessert"
    ]


# 5. GET /item/{item_name}
@app.get("/item/{item_name}")
def get_item(item_name: str):
    for item in menu:
        if item["name"].lower() == item_name.lower():
            return item

    return {"error": "Item not found"}


# 6. GET /category/{category_name}
@app.get("/category/{category_name}")
def get_category(category_name: str):
    return [
        item
        for item in menu
        if item["category"].lower() == category_name.lower()
    ]


# 7. GET /price/{item_name}
@app.get("/price/{item_name}")
def get_price(item_name: str):
    for item in menu:
        if item["name"].lower() == item_name.lower():
            return str(item["price"])

    return "Item not found"


# 8. GET /vegetarian-options
@app.get("/vegetarian-options")
def get_vegetarian_options():
    return [
        item["name"]
        for item in menu
        if item["is_vegetarian"] is True
    ]


# 9. GET /most-expensive
@app.get("/most-expensive")
def get_most_expensive():
    return max(menu, key=lambda item: item["price"])


# 10. GET /total-items
@app.get("/total-items")
def get_total_items():
    total_appetizers = len([
        item for item in menu
        if item["category"] == "appetizer"
    ])

    total_mains = len([
        item for item in menu
        if item["category"] == "main"
    ])

    total_desserts = len([
        item for item in menu
        if item["category"] == "dessert"
    ])

    return {
        "total_appetizers": total_appetizers,
        "total_mains": total_mains,
        "total_desserts": total_desserts,
        "total_all": len(menu)
    }

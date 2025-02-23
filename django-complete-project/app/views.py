from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, "app/index.html", {}) 
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape",  "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    products = [
        {"name": "Smartphone", "price": 700},
        {"name": "Watch", "price": 200},
        {"name": "Desktop", "price": 500},
        {"name": "Mac Book Pro", "price": 800},
        {"name": "Product 9", "price": 900},
        {"name": "Product 10", "price": 100},
    ]
    context = {
        "course_title": "Django Course",
        "current_date": datetime.now(),
        "user": {
            "name": "Masud Rana",
            "email": "masudrana@gmail.com",
            "is_name_shown": True,
        },
        "product_price": 199.999999,
        "random_text": "Random text for testing",
        "fruits": fruits,
        "products": products,
        "names": ["Smartphone", "Watch", "Desktop", "Mac Book Pro"],
         
    }
    

    return render(request, "index.html", context)


def aboutus(request):
    return HttpResponse("About us page")
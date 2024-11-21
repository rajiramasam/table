from django.shortcuts import render
'''from . models import Book'''
'''from . models import Student'''
'''from . models import Product'''
'''from . models import Order'''
'''from . models import Product_Details'''

'''def book(request):
    members = Book.objects.all()  # Fetch all Book objects from the database
    context = {
        'members': members,  # Context variable to be used in the template
    }
    return render(request, 'book.html', context)  # Use render to handle the template'''

'''def student(request):
    members = Student.objects.all()  # Fetch all Book objects from the database
    context = {
        'members': members,  # Context variable to be used in the template
    }
    return render(request, 'student.html', context) '''
'''def product(request):
    members = Product.objects.all()  # Fetch all Book objects from the database
    context = {
        'members': members,  # Context variable to be used in the template
    }
    return render(request, 'product.html', context)'''
'''def order(request):
    members = Order.objects.all()  # Fetch all Book objects from the database
    context = {
        'members': members,  # Context variable to be used in the template
    }
    return render(request, 'order.html', context)'''
from django.shortcuts import render, get_object_or_404
from .models import Product_Details

def product_detail(request, product_id):
    product = get_object_or_404(Product_Details, id=product_id)
    print(f"Fetched product: {product}")  # Debugging statement
    return render(request, 'product_details.html', {'product': product})

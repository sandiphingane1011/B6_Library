from urllib import request
from django.shortcuts import redirect, render 
from models import Book
from django.http import HttpResponse
import traceback
from django.contrib.auth import login, logout,authenticate
# Create your views here.



# function base view / class based view

def homepage(request):
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")                                #request----httpRequest
    if request.method ==  "POST":
        # print(request.method) 
        # print(request.POST,type(request.POST))
        if not request.POST.get("bid"):
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name, type(book_qty), book_price) 
            Book.objects.create(name=book_name, price=book_price,qty=book_qty)
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExits as err_msg:
                print (err_msg) 
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save() 
            return redirect("show_all_books")

        #statments-----
        # a = [1,2,3,4]
        #print(a)
         
        # return HttpResponse("<h3>Hi Hello</h3><h5>Good Evening...!</h5>")
    elif request.method=="GET":
        all_books = Book.objects.all()
        data = {"books":all_books}
        return render(request, template_name="home.html")
        
        
    # else :
    # return render(request,'home.html') 

# HTTP status code---200--info
# http://127.0.o.1:8000/home/    Base  URL---

def show_all_books(request):
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request, "show_books.html", context=data) 

def edit_data(request,id):
    book = Book.objects.get(id=id)
    return render(request, template_name="home.html",context={"single_book": book}) 






def delete_data(request, id):
    print(request.method)
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()  # detailed exception msg
            #print(err_msg)
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show all books")
    else:
        return HttpResponse(f"Request method: {request.method} Not allowed..! Only POST method is allowed")



from django.shortcuts import render

def view_a(request):
    return HttpResponse("in view_a")

def view_b(request):
    return HttpResponse("in view_b")

def view_c(request):
    return HttpResponse("in view_c")

def view_d(request):
    return HttpResponse("in view_d")   


# def product_video(request):
#     print("In product video")
#     return HttpResponse("video")

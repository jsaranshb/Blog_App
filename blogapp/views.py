from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import commentmodel, contactmodel, postmodel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.

# def homepage(request):
#     posts = postmodel.objects.all()
#     return render(request, 'blogapp/homepage.html', {"posts" : posts})

class HomePageView(View):
    template_name = "blogapp/homepage.html"
    
    def get(self, request):
        posts = postmodel.objects.order_by("-id")
        context = {
            "posts" : posts
        }
        return render(request, self.template_name, context)

# def single_blog(request, id):
#     post = postmodel.objects.get(id=id)
#     comments=commentmodel.objects.filter(post=post).order_by("-id")
#     context={
#         "post":post,
#         "comments":comments
#     }
#     return render(request, 'blogapp/single_blog.html', context)

class SingleBlogView(View):
    template_name = "blogapp/single_blog.html"

    def get(self, request, id):
        post = postmodel.objects.get(id=id)
        comments=commentmodel.objects.filter(post=post).order_by("-id")
        context={
            "post":post,
            "comments":comments
        }
        return render(request, self.template_name, context)

# @login_required
# @require_http_methods(["POST"])
# def add_comment(request, post_id):
#     post_obj = postmodel.objects.get(id=post_id)
#     comment_obj = commentmodel(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
#     comment_obj.save()
#     return HttpResponseRedirect(reverse('blogapp:single_blog', args=(post_id,)))

method_decorator(login_required, name="Dispatch")
class AddCommentView(View):
    template_name = "blogapp:single_blog"

    def post(self, request, post_id):
        post_obj = postmodel.objects.get(id=post_id)
        comment_obj = commentmodel(post=post_obj, owner=request.user, comment_body=request.POST["msg"])
        comment_obj.save()
        return HttpResponseRedirect(reverse(self.template_name, args=(post_id,)))

# @require_http_methods(["GET", "POST"])
# def login_user(request):
#     if request.method == "POST":
#         input_username=request.POST.get("username")
#         input_password=request.POST.get("password")
#         if not input_username or not input_password:
#             return render(request, 'blogapp/login_page.html',{"msg":"Both username and password required to login."})    
#         else:
#             user = authenticate(username=input_username, password=input_password)
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("blogapp:homepage"))
#             else:
#                 return render(request, 'blogapp/login_page.html',{"msg":"Invalid username and password combination."})
#     elif request.method == "GET":
#         msg = request.GET.get("msg")
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(reverse("blogapp:homapage"))
#         return render(request, 'blogapp/login_page.html', {"msg":msg})

class LoginView(View):

    def get(self, request):
        msg = request.GET.get("msg")
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("blogapp:homapage"))
            #return render(request, "blogapp/homepage.html")
        return render(request, 'blogapp/login_page.html', {"msg":msg})

    def post(self, request):
        input_username=request.POST.get("username")
        input_password=request.POST.get("password")
        if not input_username or not input_password:
            return render(request, 'blogapp/login_page.html',{"msg":"Both username and password required to login."})    
        else:
            user = authenticate(username=input_username, password=input_password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("blogapp:homepage"))
            else:
                return render(request, 'blogapp/login_page.html',{"msg":"Invalid username and password combination."})

# @require_http_methods(["GET", "POST"])
# def sign_up(request):
#     if request.method == "POST":
#         username=request.POST.get("username")
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         confirm_password=request.POST.get("confirm_password")
#         if not username or not email or not password or not confirm_password :
#             return render(request, 'blogapp/sign_up.html',{"msg":"All field are required to register."})
#         elif password != confirm_password :
#             return render(request, 'blogapp/sign_up.html',{"msg":"Password and confirm-password should be same to register."})
#         elif User.objects.filter(username=username).exists() :
#             return render(request, 'blogapp/sign_up.html',{"msg":"Username already exists, Please try another username."})
#         elif User.objects.filter(email=email).exists() :
#             return render(request, 'blogapp/sign_up.html',{"msg":"Account with this email already exists, Please try another email."})
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             return render(request, 'blogapp/login_page.html',{"msg":"Registered Successfully, Please Login ..."})
#     else:
#         return render(request, "blogapp/sign_up.html")

class SignUpView(View):

    def get(self, request):
        return render(request, "blogapp/sign_up.html")

    def post(self, request):
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if not username or not email or not password or not confirm_password :
            return render(request, 'blogapp/sign_up.html',{"msg":"All field are required to register."})
        elif password != confirm_password :
            return render(request, 'blogapp/sign_up.html',{"msg":"Password and confirm-password should be same to register."})
        elif User.objects.filter(username=username).exists() :
            return render(request, 'blogapp/sign_up.html',{"msg":"Username already exists, Please try another username."})
        elif User.objects.filter(email=email).exists() :
            return render(request, 'blogapp/sign_up.html',{"msg":"Account with this email already exists, Please try another email."})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request, 'blogapp/login_page.html',{"msg":"Registered Successfully, Please Login ..."})

def logout_user(request):
    logout(request)
    #return HttpResponseRedirect(reverse("blogapp:login_user"))   
    return render(request, 'blogapp/login_page.html', {})

# @login_required
# def user_blog(request):
#     if request.method == "POST":
#         Tittle = request.POST.get("title")
#         Summary = request.POST.get("summary")
#         Postbody = request.POST.get("content")
#         Postimage =  request.FILE.get("image")
#         new_blog = postmodel(post_title=Tittle, post_summary=Summary, post_body=Postbody, post_image=Postimage)
#         if not Tittle or not Summary or not Postbody or not Postimage :
#             return render(request, 'blogapp/user_blog.html',{"msg":"All field are required to post a blog."})
#         elif postmodel.objects.filter(post_title=Tittle).exists() :
#             return render(request, 'blogapp/user_blog.html',{"msg":"Title already exists, Please use another title."})
#         else:
#             new_blog.save()
#             return HttpResponseRedirect(reverse("blogapp:homepage"))
#     else:
#         return render(request, 'blogapp/user_blog.html')

method_decorator(login_required, name="dispatch")
class UserBlogView(View):

    def get(self, request):
        return render(request, 'blogapp/user_blog.html')

    def post(self, request):
        Tittle = request.POST.get("title")
        Summary = request.POST.get("summary")
        Postbody = request.POST.get("content")
        Postimage =  request.FILE.get("image")
        new_blog = postmodel(post_title=Tittle, post_summary=Summary, post_body=Postbody, post_image=Postimage)
        if not Tittle or not Summary or not Postbody or not Postimage :
            return render(request, 'blogapp/user_blog.html',{"msg":"All field are required to post a blog."})
        elif postmodel.objects.filter(post_title=Tittle).exists() :
            return render(request, 'blogapp/user_blog.html',{"msg":"Title already exists, Please use another title."})
        else:
            new_blog.save()
            return HttpResponseRedirect(reverse("blogapp:homepage"))

def fav_blog(request):
    s=request.GET.get("search", "")
    posts = postmodel.objects.filter(post_title__contains = s)
    return render(request, 'blogapp/homepage.html', {"posts" : posts})

# @require_http_methods(["GET", "POST"])
# def contact(request):
#     if request.method == "POST":
#         Name = request.POST.get("name")
#         Email = request.POST.get("email")
#         Mobile_Number = request.POST.get("mobile")
#         Query = request.POST.get("mssg")
#         contact_obj = contactmodel(Name=Name, Email=Email, Mobile_Number=Mobile_Number, Query=Query)
#         if not Name or not Email or not Query :
#             return render(request, "blogapp/contact.html", {"msg":"All fields are necessuary to contact with us."})
#         elif contactmodel.objects.filter(Email=Email).exists():
#             return render(request, "blogapp/contact.html", {"msg":"Email already exists Please use another email."})
#         else:
#             contact_obj.save()
#             return render(request, "blogapp/contact.html", {"msg":"Query Submitted."})
#     else:
#         return render(request, "blogapp/contact.html")

method_decorator(login_required, name="didspatch")
class ContactView(View):
    template_name = "blogapp/contact.html"
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Mobile_Number = request.POST.get("mobile")
        Query = request.POST.get("mssg")
        contact_obj = contactmodel(Name=Name, Email=Email, Mobile_Number=Mobile_Number, Query=Query)
        if not Name or not Email or not Query :
            return render(request, "blogapp/contact.html", {"msg":"All fields are necessuary to contact with us."})
        elif contactmodel.objects.filter(Email=Email).exists():
            return render(request, "blogapp/contact.html", {"msg":"Email already exists Please use another email."})
        else:
            contact_obj.save()
            return render(request, "blogapp/contact.html", {"msg":"Query Submitted."})

        



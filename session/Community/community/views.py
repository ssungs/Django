from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Category, Article, UserPro
from django.contrib import auth

# Create your views here.

def index(request) :
    categories = Category.objects.all()
    return render(
        request,
        'index.html',
        {
            'categories' : categories
        }
    )

def category(request, category_pk) :
    category = get_object_or_404(Category, pk=category_pk)
    articles = Article.objects.filter(category=category)

    article_list = []

    for article in articles:
        if (article.is_deleted == False) :
            article_list.append(article)

    return render(
        request,
        'category.html',
        {
            'category' : category,
            'articles' : article_list
        }
    )

def article(request, article_pk) :
    article = get_object_or_404(Article, pk=article_pk)

    return render(
        request,
        'article.html',
        {
            'article': article
        }
    )

def back1(request):
    
    return redirect('index')

def back(request, article_pk):
    article = Article.objects.filter(pk=article_pk).first()
    category_pk = article.category.pk

    return redirect('category', category_pk)


def add(request) :
    categories = Category.objects.all()

    context = {
        'categories' : categories,
        'error' : {
            'state' : False,
            'msg' : ''
        }
    }

    if request.method == 'POST' : 
        category_pk = request.POST['category_pk']
        title = request.POST['title']
        content = request.POST['content']
        
        if (title and content) :

            target_category = get_object_or_404(Category, pk=category_pk)

            article = Article.objects.create(
                title=title,
                content=content,
                category=target_category
            )
            return redirect('article', article.pk)
        
        else :
            context['error']['state'] = True
            context['error']['msg'] = '모든 항목을 채워주세요'

    return render(request, 'add.html', context)

def add1(request, category_pk):

    category = Category.objects.filter(pk=category_pk).first()

    target_category = get_object_or_404(Category, pk=category_pk)

    target_user = UserPro.objects.filter()

    context = {
        'category' : category,
        'error' : {
            'state' : False,
            'msg' : ''
        }
    }

    if request.method == 'POST' : 
        title = request.POST['title']
        content = request.POST['content']
        
        if (title and content) :


            article = Article.objects.create(
                title=title,
                content=content,
                category=target_category,
                name=target_user.
            )
            return redirect('article', article.pk)
        
        else :
            context['error']['state'] = True
            context['error']['msg'] = '모든 항목을 채워주세요'

    return render(request, 'add1.html', context)


def signup(request):
    
    if request.method == 'POST': # POST 메소드 확인
        userid = request.POST['userid']
        password = request.POST['password']
        password_check = request.POST['password_check']
        name = request.POST['name']
        city = request.POST['city']
        age = request.POST['age']
        user = User.objects.filter(username=userid)
        
        if (userid and password and password_check): # 모든항목 작성했는지 확인

            if (len(user)==0): # 존재하는 아이디 확인

                if (password) == password_check: # 비밀번호 확인
                    # create user model
                    user = User.objects.create_user(
                        username = userid,
                        password = password,
                    )

                    user_pro = UserPro.objects.create(
                        user = user,
                        user_pro = user,
                        name = name,
                        city = city,
                        age = age
                    )

                    auth.login(request, user)

                    return redirect('index')

                else:
                    context = {
                        'error': {
                            'state' : True,
                            'msg': '비밀번호가 다릅니다.'
                        }
                    }
                    return render(request, 'signup.html', context)

            else:
                context = {
                    'error': {
                        'state' : True,
                        'msg': '이미 존재하는 아이디 입니다.'
                    }
                }
                return render(request, 'signup.html', context)

        else:
            context = {
                'error': {
                    'state' : True,
                    'msg': '필수 항목을 작성해 주세요.'
                }
            }

            return render(request, 'signup.html', context)
        
    return render(request, 'signup.html')

def login(request):

    context = {
        'error' : {
            'state' : False,
            'msg' : ''
        }
    }

    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = User.objects.filter(username=userid)

        if (not userid) and (not password):
            print(2)
            context['error']['state'] = True
            context['error']['msg'] = '아이디나 비밀번호를 입력하세요.'
            return render(request, 'login.html', context)
     
        if len(user) == 0:
            print(3)
            context['error']['state'] = True
            context['error']['msg'] = '존재하지 않는 아이디 입니다.'
            return render(request, 'login.html', context)

        auth_user = auth.authenticate(
            username=userid,
            password=password
        )

        if auth_user == None:
            context['error']['state'] = True
            context['error']['msg'] = '비밀번호가 틀렸습니다.'
            return render(request, 'login.html', context)

        if (auth_user):
            auth.login(request, auth_user)
            return redirect('index')

        # if auth_user.password != password:
        #     context['error']['state'] = True
        #     context['error']['msg'] = '비밀번호가 틀렸습니다.'
        #     return render(request, 'login.html', context)
        

        # try:
        #     print(user)
            
        #     print(1)
        # except :
        #     print(2)
        #     context['error']['state'] = True
        #     context['error']['msg'] = '존재하지 않는 아이디 입니다.'
        #     return render(request, 'login.html', context)

        # if (not password) :
        #     print(3)
        #     context['error']['state'] = True
        #     context['error']['msg'] = '아이디나 비밀번호가 틀렸습니다.'
        #     return render(request, 'login.html', context)
        
        # print(user)
        # print(5)
        # print(auth_user)

        # if (auth_user):
        #     print(4)
        #     auth.login(request, auth_user)
        #     return redirect('index.html')

    return render(request, 'login.html', context)


def logout(request):

    auth.logout(request)

    return redirect('index')
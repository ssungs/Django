from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Category, Article, UserPro, Comment, Like
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

    comments = Comment.objects.filter(article=article)
    return render(
        request,
        'article.html',
        {
            'article': article,
            'comments': comments
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

    target_user = UserPro.objects.get(user=request.user)
    # print(target_user)

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
                category=category,
                writer=target_user
            )
            # print(article)
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
            # print(2)
            context['error']['state'] = True
            context['error']['msg'] = '아이디나 비밀번호를 입력하세요.'
            return render(request, 'login.html', context)
     
        if len(user) == 0:
            # print(3)
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

def comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = UserPro.objects.get(user=request.user)
    content = request.POST['comment']
    # pk = article_pk
    # try:
    #     pass
    # if not content:
    #     context = {
    #         'state': True,
    #         'msg': '내용을 입력하세요.'
    #     }
    #     return render(request, 'article.html', context)

    # except IntegrityError:
    #     pass

    Comment.objects.create(
        article = article,
        writer = user,
        content = content,
        # pk = pk
    )
    return redirect('article', article_pk)

def writer(request, writer_pk):

    user = Comment.objects.get(writer_pk=writer_pk)
    
    my_comments = Comment.objects.filter(writer__user=user)
    
    content = {
        'user': user,
        'my_comments': my_comments
    }
    return render(request, 'writer.html', content)

def like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    user = UserPro.objects.get(user=request.user)
    comment = Comment.objects.get(writer=request.user)
    # like = Like.objects.filter(user=user).first()
    print(like)
    Like.objects.create(
        article = article,
        user = user,
        comment = comment
    )
    return redirect('article', article_pk)
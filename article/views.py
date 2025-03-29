from django.shortcuts import render

from .models import Article
# Create your views here.



    


articles = Article.objects.all()

def contact(request):
    
    context={
        "data1":"contact our head office for more detailes",
        "data2": "91+84512677842",
        'title':'TIMES OF INDIA',
        
    }
    return render(request,'pages/contact.html',context)

def home(request):
    result = articles
    search=request.GET.get('search')
    print(search)
    if search:
        result = [article for article in articles if search.lower() in article.description.lower()  
                ]
    else:
        print('no data found')
    
    context={
        'title':'Times of india',
        'data3':'latest News',
        'articles': result,
        'data4': "get latests news faster and stay updated",
        'data5': "install the app"
        
    }
    return render(request,'pages/home.html',context)

def about(request):
    
    context={
        'data6':'''Times of India is global news article 
                which provides you with current news around the world'''
     }
    
    return render(request,'pages/about.html',context)


def article(request,id):
    
    data=None
    for article in articles:
        if article.id == id:
            data = article
            break
        
    context={
        "title":"detailed_article_page",
        'article': data,
    }
    
    return render(request,'pages/article.html',context)

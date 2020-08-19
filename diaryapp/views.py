from django.shortcuts import render
from .models import Diary
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.


def main(request):
    diary_all = Diary.objects.all().order_by("-id") # 쿼리셋, 객체목록 가져오기
    # blog_all = blog.all()
    paginator =Paginator(diary_all, 3) #3개씩 쪼개서 페이지에 보여준다.
    # 8000/detail/?page='3' 이런식으로 넘어간다. 그래서 현재 페이지가 몇번인지 알아야한다
    page=request.GET.get('page') #페이지는 항상 GET방식으로 받는다 이러면 현재 페이지가 몇번인지 알수있다
    posts= paginator.get_page(page) #가지고 온 페이지를 posts에 저장한다
    return render(request, "main.html", {"diary": posts}) #page에 관련된 객체 넘겨줌


def detail(request, diary_id):
    diary_all = Diary.objects.all().order_by("-id")
    count = Diary.objects.count()
    diary = get_object_or_404(Diary, page_number=diary_id)
    return render(request, "detail.html", {"diary_detail": diary, "row_count": count})


def next(request, diary_id):
    count = Diary.objects.count()

    if diary_id + 1 > count:
        return redirect("/detail/1")
    else:
        return redirect("/detail/" + str(diary_id + 1))


def before(request, diary_id):
    count = Diary.objects.count()
    if diary_id - 1 == 0:
        return redirect("/detail/" + str(count))
    else:
        return redirect("/detail/" + str(diary_id - 1))


def write(request):
    if request.method == "POST":
        diary = Diary()
        diary.title = request.POST["title"]
        try:
            diary.image = request.FILES["image"]
        except:
            pass
        diary.body = request.POST["body"]
        diary.pub_date = timezone.datetime.now()
        diary.page_number = Diary.objects.count() + 1
        diary.save()
        return redirect("/detail/" + str(diary.page_number))
    else:
        return render(request, "write.html")


def rewrite(request, diary_id):
    if request.method == "POST":
        diary = get_object_or_404(Diary, page_number=diary_id)
        diary.title = request.POST["title"]
        diary.body = request.POST["body"]
        diary.pub_date = timezone.datetime.now()
        diary.save()
        return redirect("/detail/" + str(diary_id))
    else:
        diary = get_object_or_404(Diary, page_number=diary_id)
        return render(request, "rewrite.html", {"diary": diary})


def remove(request, diary_id):
    diary = get_object_or_404(Diary, page_number=diary_id)
    diary.delete()

    object_all = Diary.objects.all()
    for item in object_all:
        if item.page_number > diary_id:
            item.page_number = item.page_number - 1
            item.save()
        else:
            pass

    return redirect("/")

def search(request):
    diarys = Diary.objects.all().order_by('-id')
    q = request.POST.get('q', "")

    if q:
        diarys = diarys.filter(title__icontains=q)
        return render(request, 'search.html', {'diarys': diarys, 'q' : q})
    else:
        return render(request, 'search.html')

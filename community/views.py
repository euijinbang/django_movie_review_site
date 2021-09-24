# from community.forms import ReviewForm
from community.models import Review
from community.forms import ReviewForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request, 'community/index.html', context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("community:index")
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, "community/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk) # 요청받은 pk 하나 꺼내서
    context = {
        'review':review, # context에 담아서
    }
    return render(request, "community/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("community:index")
    else:
        form = ReviewForm(instance=review) # 원래 들어있던 정보!! 위에서 가져온거~ 왜 instance라 하지?
    context = {
        'form' : form,
    }
    return render(request, "community/update.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.mothod == "POST":
        review.delete() # delete 메서드 사용
        return redirect("community:index")
    return redirect("community:detail", review.pk)
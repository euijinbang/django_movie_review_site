from django.shortcuts import get_object_or_404, redirect, render
# 1 Model 
from community.models import Review
# 2 ModelForm
from community.forms import ReviewForm
# 3 HTTP Decorator
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# 4 Auth Decorator
from django.contrib.auth.decorators import login_required, permission_required


# 인덱스 함수 : 등록한 리뷰를 Model에서 ORM으로 불러온다.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'community/index.html', context)

# CREATE : GET, POST 방식으로 분기처리
@require_http_methods(["GET", "POST"]) 
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            # review = form.save()
        return redirect('community:index')
        # return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/create.html', context)

# READ : 해당 1개의 게시글 pk 정보로 찾는다.
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)#  요청받은 pk 하나 꺼내서
    # review = Review.objects.get(pk=pk) 
    context = {
        'review' : review, # context에 담아서
    }
    return render(request, 'community/detail.html', context) # html로 렌더링

# UPDATE : GET, POST 방식으로 분기처리
@require_http_methods(["GET", "POST"])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = ReviewForm(instance=review) # 기존 정보를 instance(class 문법)에 담는다
    context = {                            # 폼과 pk 정보를 컨텍스트에 담는다
        'review' : review,
        'form' : form,
    }
    return render(request, 'community/update.html', context)


# DELETE : POST방식, 해당 게시글을 삭제하는 메서드를 사용
@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete() # delete 메서드 사용
        return redirect('community:index')
    return redirect('community:detail', review.pk)
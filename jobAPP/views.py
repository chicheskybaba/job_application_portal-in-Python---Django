from django.shortcuts import render, get_object_or_404
from .models import Job_Model, Application
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ApplicationForm
from django.views.decorators.http import require_POST

# Create your views here.





def job_list(request):
    job_list = Job_Model.published.all()
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'job/post/list.html', {'posts': posts})
    
    
    
    
    
def job_detail(request, id):
    # Form for users to comment
    form = ApplicationForm()
    post = get_object_or_404(Job_Model, id=id, status=Job_Model.Status.PUBLISHED)
    return render(request, 'job/post/detail.html', {'post': post, 'form': form})
    

    
    
    
@require_POST
def post_application(request, post_id):
    post = get_object_or_404(Job_Model, id=post_id, status=Job_Model.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = ApplicationForm(request.POST, request.FILES)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
        
    return render(request, 'job/post/application.html', {'post': post, 'form': form, 'comment': comment})
        
        
        
        
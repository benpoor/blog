from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from polls.models import Poll

# Create your views here.
def index(request):
    last_poll_list  = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context  = RequestContext(request, {
        'last_poll_list':last_poll_list,
    })
    return HttpResponse(template.render(context))

def detail(request, poll_id):
    # try:
    #     poll  = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    # return render(request, 'polls/detail.html', {'poll':poll})
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})
1
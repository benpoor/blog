from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
import json

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

def vote(request, poll_id):
    # return HttpResponse("vote is :%s" % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message':"you didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll':poll})

def json(request):
    response_data = {}
    response_data['result'] = 'a'
    response_data['message'] = 'yyyy'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
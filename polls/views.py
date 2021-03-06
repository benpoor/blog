from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from polls.models import Poll, Choice, User
from polls.util import MyJsonEncoder
import json

# Create your views here.
# def index(request):
#     last_poll_list  = Poll.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context  = RequestContext(request, {
#         'last_poll_list':last_poll_list,
#     })
#     return HttpResponse(template.render(context))
#
# def detail(request, poll_id):
#     # try:
#     #     poll  = Poll.objects.get(pk=poll_id)
#     # except Poll.DoesNotExist:
#     #     raise Http404
#     # return render(request, 'polls/detail.html', {'poll':poll})
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll':poll})
#
# def vote(request, poll_id):
#     # return HttpResponse("vote is :%s" % poll_id)
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'poll': p,
#             'error_message':"you didn't select a choice",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
#
# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll':poll})

def get_json(request):
    response_data = {}
    response_data['result'] = 'a'
    response_data['message'] = 'yyyy'
    datas = []
    datas.append(response_data)

    p = Poll.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    u = MyJsonEncoder()
    return HttpResponse(json.dumps(u.encode(p)), content_type="application/json")
    # result = "{'id': 1, 'name': 'sss'}"
    # return HttpResponse(result)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'last_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return  Poll.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

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

class UserView(generic.ListView):
    template_name = 'polls/user.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return Poll.objects[:5]

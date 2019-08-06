from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Stock, User, TargetAllocation

def index(request):
    stock = get_object_or_404(Stock, pk=1)
    return render(request, 'invest/index.html', {'stock': stock})


def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'invest/profile.html', context)

def allocate(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    for alloc in user.targetallocation_set.all():
        stock = alloc.stock
        allocPerc = alloc.allocPercentage/100
        bidString = "bidvalue"+str(stock)
        posString = "currentposition"+str(stock)
        bidValue = request.POST[bidString]
        posValue = request.POST[posString]
        print(stock)

    return 'Hey'
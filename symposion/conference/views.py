from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import get_user_model

from account.decorators import login_required


@login_required
def user_list(request):

    if not request.user.is_staff:
        raise Http404()

    return render(request, "symposion/conference/user_list.html", {
        "users": get_user_model().objects.all(),
    })

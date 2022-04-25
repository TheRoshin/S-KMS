from django.shortcuts import render
from backend.models import postQus
from django.db.models import Q

def searchResult(self):
    query = self.GET.get("search")
    queryset = postQus.objects.filter(post_title__icontains = query)

    return render(self, 'templates/searchResults.html', {'list': queryset,})
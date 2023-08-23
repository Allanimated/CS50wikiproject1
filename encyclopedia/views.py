from django.shortcuts import render, redirect
from django.urls import reverse
from . import util
import markdown2
from markdown2 import Markdown
import random




def index(request):
    entries = util.list_entries()
    context = {'entries':entries}
    return render(request, "encyclopedia/index.html", context)



def entry(request, title):

    contents = util.get_entry(title)
    html_content = markdown2.markdown(contents)

 
    context = {'title': title, 'contents':html_content }
    
    if contents:
        return render(request, "encyclopedia/entry.html", context)
    else:
        return None

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q', '').lower()
        entries = util.list_entries()
        results = []
        
        for entry in entries:
            if entry.lower() == query:
                # Redirect the user to the page that matches the query
                return redirect(reverse('encyclopedia:entry', args=[entry]))

            if query in entry.lower():
                
                results.append(entry)
        
        if results:
            #takes the user to a search results page that displays a list of all encyclopedia entries that have the query as a substring
            context = {'query': query, 'results': results}
            return render(request, "encyclopedia/search.html", context)
        else:
            # Return an error page if the query has not been found
            return render(request, "encyclopedia/error.html", {'message':'The entry has not been found!!!'})
def new_page(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/newpage.html")
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        title_exist = util.get_entry(title)
        if title_exist is not None:
            #checks to see if the title posted exists
            return render(request, "encyclopedia/error.html", {'message': 'Entry page already exists'})
        else:
            util.save_entry(title, contents)
            html_content = markdown2.markdown(contents)
            context = {'title': title, 'contents': html_content}
            return render(request, "encyclopedia/entry.html", context)


def edit_entry(request, title):
    if request.method == 'GET':
         contents = util.get_entry(title)
         context = {'title': title, 'contents':contents }
         return render(request, "encyclopedia/edit.html", context)
    if request.method == 'POST':
        entry_title = request.POST.get('title')
        contents = request.POST.get('contents')
        util.save_entry(entry_title, contents)
        html_content = markdown2.markdown(contents)
        context = {'title': title, 'contents': html_content}
        return render(request, "encyclopedia/entry.html", context)
    
def random_page(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    contents = util.get_entry(entry)
    html_content = markdown2.markdown(contents)

    context = {'entry': entry, 'contents': html_content}
    return redirect(reverse('encyclopedia:entry', args=[entry]))









         
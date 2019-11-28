from django.shortcuts import render, redirect
from .models import Search, Find
from django.contrib import messages
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def dash_board(request):
     if request.method == 'POST':
          textarea_data = request.POST['comment'] #fetching the data stroing in variable.
          textarea_data = textarea_data.lower()   #make it as lowercase.
          textarea_data = re.sub(r'[^\w\s]',' ', textarea_data) #Remove  puncuations.
          lines = [l for l in textarea_data.split('\r\n\r\n') if l]
          for line in lines:
               print(line)
               get_from_search_model = Search.objects.create(text=line)
               seperate = line.split(' ')
               splits = list(set(seperate))
               ''' 
                    First It can be assinged in to set for removing duplicates.
                    then assign into lists.
               '''
               for split in splits:
                    create, created = Find.objects.get_or_create(words=split)
                    '''
                         created is used for ==> If the object is already there it can be get the objects 
                         but not assign.If the object is not there it can be create the object and add it to the "location(model field)".
                    '''
                    create.location.add(get_from_search_model) #ManyToMany Field.
          return render(request, 'email.html', {})
     else:
          return render(request, 'email.html', {})
          
def next(request):
     if request.method == 'POST':
          search_data = request.POST['search'] # fetching the data.
          search_data = search_data.lower()
          b =  "please search something"
          unique = Find.objects.filter(words=search_data).first()
          ''' 
             We stored the unique words in database. 
             In that database we take the first object.
          ''' 
          if (search_data != ""):
               if unique:
                    return render(request, 'search.html', {'valids':unique.location.all().values('text')}) #
               else:
                    messages.info(request, 'No Results found')
                    return render(request, 'search.html')
          else:
               return render(request,'search.html', {"empty":[b]})
     else:
          return render(request,'search.html')
         
     
def clear(request):
     Search.objects.all().delete()
     return redirect('next')


def back(request):
     return reidrect('/')





if request.method == 'POST':
          search = request.POST['search']
          b = "Please Serach something"
         
          if (search != ""):
               if search:
                    a = Search.objects.filter(text__contains=search)
                    
                    print('Highlighted')
                    
                    if a:
                         
                         return render(request,'search.html', {"messages":a})
                         print('search')
                    else:
                         messages.info(request, 'No results found ') 
                         return render(request,'search.html')
           
               else:
                    return render(request,'search.html')
          else:
            return render(request,'search.html', {"messages":[b]})
      

     else:
         return render(request,'search.html')










counts = words
           count = counts.count
           z = {}
           for count in counts:
               if count in z:
                   z[count] += 1
               else:
                   z[count] = 1
           for key, value in z.items():
                print('({} ,{})'.format(key, value))
          



##pagination:

   paginator = Paginator(unique, 3)
                    page = request.GET.get('page')
                    contacts = paginator.get_page(page)
                    try:
                         posts = paginator.page(page)
                    except PageNotAnInteger:
                         posts = paginator.page(1)
                    except EmptyPage:
                         posts = paginator.page(paginator.num_pages)
                    context = {
                         posts:'unique'
                    }



##html view



{% if posts.has_other_pages %}
        


        <ul class="pagination">
          {% if posts.has_previous %}
               <li><a href="?page={{ posts.previous_page_number }}">&laquo;</a></li>
          {% else %}
               <li class="disabled"><span>&laquo;</span></li>
          {% endif %}
          {% for post in posts.page_range %}
               {% if posts.number == post %}
                    <li class="page-item active">
                    <a href="?page={{ post }}" class="page-link">{{ post }}</a>
                    </li>
               {% else %}
                    <li class="page-item">
                    <a href="?page = {{ post }}" class="page-link">{{ p }}</a>
                    </li>
               {% endif %}

          {% endfor %}
          {% if posts.has_next %}
               <li><a href="?page={{ posts.next_page_number }}">&raquo;</a></li>
          {% else %}
               <li class="disabled"><span>&raquo;</span></li>
          {% endif %}
      </ul>




     lines = [l for l in textarea_data.split('\r\n\r\n') if l]
          for line in lines:
               print(line)



               lines = []
          lines = textarea_data.split('\n')
          for line in lines:
               print(line)
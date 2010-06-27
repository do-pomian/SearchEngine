# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from SearchEngine.mysearchengine.models import Store
from SearchEngine.mysearchengine.models import StoreDetails
from SearchEngine.mysearchengine.models import Products 
from SearchEngine.mysearchengine.models import Producers
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from SearchEngine.mysearchengine.contactform import ContactForm

def index (request):
    store_list = Store.objects.all()
    t = loader.get_template('mysearchengine/index.html')
    location = request.META['REMOTE_ADDR']
    c = Context ({
                  'store_list': store_list,
                  'location': location
                  })
    return HttpResponse (t.render(c))

def detail (request, Store_id):
    # store_details = get_object_or_404(StoreDetails, Store=Store_id)
    try:
        store_details = StoreDetails.objects.get(Store=Store_id)
        store = Store.objects.get(pk=Store_id)
    except StoreDetails.DoesNotExist:
        return render_to_response('mysearchengine/store_details.html', {'store_details': ''}, context_instance=RequestContext(request))
    return render_to_response('mysearchengine/store_details.html', {'store_details': store_details, 'store' : store}, context_instance=RequestContext(request))

def results (request):
    search_input = request.GET['mysearch']
    try:
        products = Products.objects.all().filter(ProductName__icontains=search_input)
        output = []
        producers = []
        stores = []
        o1 = []
        for product in products:
            producer = Producers.objects.get(pk=product.Producer_id)
            producers.append (producer)
            store = Store.objects.get(pk=product.Store_id)
            stores.append(store)
            o1 = {'ProductName': product.ProductName, 'Price': product.Price, 'ProducerName': producer.ProducerName, 'StoreName': store.StoreName}           
            output.append(o1)
    except Products.DoesNotExist:
        return render_to_response('mysearchengine/results.html', {'product': ''}, context_instance=RequestContext(request))
    return render_to_response('mysearchengine/results.html', {'output': output}, context_instance=RequestContext(request))

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    
    return render_to_response ('mysearchengine/contact.html', 
                               {
                                'form': form,
                                })
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

from forms import CompanyData
import util

def home(request):
    return render_to_response("market/homepage.html", {'site_name': settings.SITE_NAME}, context_instance=RequestContext(request))

def valuate(request):
    if request.method == "GET":
        initial ={'name': 'Ra Vee Inc',
                   'duration': 5,
                   'ebit': 100000,
                   'depreciation':100,
                   'amortization': 200,
                   'nwc_change':300,
                   'capx': 400,
                   'tax_rate':10,
                   'ltgr':4,
                   'stgr':8,
                   'discount_rate':10,
                   }
        dataform = CompanyData(initial=initial)
        return render_to_response("market/valuate.html", {'dataform': dataform }, context_instance=RequestContext(request))
    elif request.method == "POST":
        try:
            dataform = CompanyData(request.POST)
            if dataform.is_valid():
                value = util.valuate(dataform.cleaned_data)
                ret = "You will be rich if you buy "
                company = dataform.cleaned_data.get('name')
                return render_to_response("market/showvalue.html", {'company': company, 'value': value }, context_instance=RequestContext(request))
            else:
                return render_to_response("market/valuate.html", {'dataform': dataform }, context_instance=RequestContext(request))
        except Exception as e:
            print e
            return HttpResponse("Give me the right information please")



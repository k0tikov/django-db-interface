from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q
from datetime import date

import json
from .models import *
from django.views import View
from showing.forms import *
import xlsxwriter
from excel_response import ExcelResponse
from .functions import writeToExcel
from io import StringIO
import io
import six



@login_required(login_url="http://127.0.0.1:8000")
def mainpage(request):
    return render(request, 'mainpage.html')


@login_required(login_url="http://127.0.0.1:8000")
def suppliers_table(request):
    template_name = 'suppliers-table.html'
    get_request = request.path
    cut_get_request = get_request[(len(get_request) - 5):(len(get_request) - 1)]
    #table_all_data = List_of_regedit_buy.objects.all().filter(date_of_completion=cut_get_request).order_by('expiration')
    table_all_data = List_of_regedit_buy.objects.all().filter(date_of_completion=cut_get_request)
    if 'excel' in request.POST:
        today = date.today()
        filename = 'table-list-%s.xlsx' % today.strftime("%Y-%m-%d")
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        xlsx_data = writeToExcel(table_all_data)
        response.write(xlsx_data)
        return response
    args = {'table_all_data': table_all_data}
    return render(request, template_name, args)


@login_required(login_url="http://127.0.0.1:8000")
def registry(request):
    return HttpResponseRedirect('/registry-loaded')
@login_required(login_url="http://127.0.0.1:8000")
def registry_loaded(request):
    date_teg = List_of_regedit_buy.objects.all().distinct('date_of_contract')
    return render(request, 'registry-loaded.html', {'date_teg': date_teg})


#@login_required(login_url="http://127.0.0.1:8000")
class Search(View):
    template_name = 'advanced-search-form.html'

    def get(self,request):
        form = SearchForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self,request):
        form = SearchForm(request.POST)
        company_name = form['q'].value()
        tags = form['checkbox_input'].value()
        start_year = form['start_year'].value()
        end_year = form['end_year'].value()
        # Find the company by name
        criterion_1 = Q(name_of_buyer__iexact=company_name)
        # Find data by tags
        criterion_2 = Q(tags__in=tags)
        # Set timeline
        criterion_3 = Q(date_of_completion__gte=start_year)
        # End time
        criterion_4 = Q(date_of_completion__lte=end_year)
        if company_name != "":
            take_data = List_of_regedit_buy.objects.all().filter(criterion_1 & criterion_2 & criterion_3 & criterion_4).order_by('date_of_completion')
        else:
            take_data = List_of_regedit_buy.objects.all().filter(criterion_2 & criterion_3 & criterion_4).order_by('date_of_completion')
        if 'excel' in request.POST:
            # response = HttpResponse(content_type='application/vnd.ms-excel')
            today = date.today()
            filename = 'table-list-%s.xlsx' % today.strftime("%Y-%m-%d")
            response = HttpResponse(content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
            xlsx_data = writeToExcel(take_data)
            response.write(xlsx_data)
            return response
        args = {'form': form, 'take_data': take_data}
        return render(request, self.template_name, args)


class SearchJson(View):
    def get(self, request):
        q = request.GET.get('q', 'tables_found.html')
        taglist = []
        # Searching for values
        tags = List_of_regedit_buy.objects.filter(name_of_buyer__icontains=q)
        # Creation(filling) new array
        for tag in tags:
            new = {'q': tag.name_of_buyer}
            taglist.append(new)
        # Deleting similar values
        n = 1 
        while n < len(taglist):
             for i in range(len(taglist) - n):
                  if taglist[i] == taglist[i+1]:
                       taglist.remove(taglist[i])
             # Counting
             n += 1
        return HttpResponse(json.dumps(taglist), content_type='application/json')


# Create your views here.



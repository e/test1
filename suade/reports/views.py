# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from weasyprint import HTML


def home(request):
    return render(request, 'report.html', {})


def pdf_report(request, id=None):
    if not id:
        return render(request, 'report.html', {})
    else:
        html_template = get_template('report.html')
        rendered_html = html_template.render(
            {}).encode(encoding="UTF-8")
        pdf_file = HTML(string=rendered_html).write_pdf()
        http_response = HttpResponse(pdf_file, content_type='application/pdf')
        http_response['Content-Disposition'] = 'filename="report.pdf"'
        return http_response

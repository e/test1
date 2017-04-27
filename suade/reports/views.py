# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from weasyprint import HTML

from reports.models import Report


def home(request):
    return render(request, 'report.html', {})


def pdf_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    data = json.loads(report.type)
    html_template = get_template('report.html')
    rendered_html = html_template.render(
        data).encode(encoding="UTF-8")
    pdf_file = HTML(string=rendered_html).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="report.pdf"'
    return http_response

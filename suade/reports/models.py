# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Report(models.Model):
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'reports'

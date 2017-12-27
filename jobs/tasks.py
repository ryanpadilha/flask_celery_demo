#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务
"""

from app import celery


@celery.task(name='tasks.add_together')
def add_together(a, b):
    print('job tasks.add_together')
    return a + b
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.widgets import TextInput


class ColorFieldWidget(TextInput):

    class Media:
        css = {
            'all': ("colorful/colorPicker.css",)
        }
        js = ("colorful/jQuery.colorPicker.js",)

    input_type = 'color'

    def render(self, name, value, attrs={}):
        if 'id' not in attrs:
            attrs['id'] = "id_%s" % name
        return super(ColorFieldWidget, self).render(name, value, attrs)

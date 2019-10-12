from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import *

from ..models import *


class SubcategoryListAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'subcategories': [],
            'depth': None
        }

        category_pk = self.request.GET.get('category_pk')
        if category_pk:
            subcategories = get_object_or_404(Category, pk=category_pk)
            data['depth'] = 0
        else:
            subcategory_pk = self.request.GET.get('subcategory_pk')
            subcategories = get_object_or_404(Subcategory, pk=subcategory_pk)
            data['depth'] = self.get_subcategory_depth(subcategory_pk)

        for subcategory in subcategories.subcategories.all():
            data['subcategories'].append({
                'pk': subcategory.pk,
                'name': subcategory.name
            })
        return JsonResponse(data)

    def get_subcategory_depth(self, subcategory_pk):
        subcategory = get_object_or_404(Subcategory, pk=subcategory_pk)
        depth = 1
        while not subcategory.category:
            subcategory = subcategory.subcategory
            depth += 1
        return depth

from .models import Product
from django.views import generic


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

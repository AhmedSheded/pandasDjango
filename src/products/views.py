from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
# Create your views here.


def chart_select_view(request):
    qs = Product.objects.all().values()
    qs2 = Purchase.objects.all().values()
    product_df = pd.DataFrame(qs)
    purchase_df = pd.DataFrame(qs2)
    # qs2 = Product.objects.all().values_list()
    product_df['product_id'] = product_df['id']
    df = pd.merge(purchase_df, product_df, on='product_id')
    context = {
        'products': product_df.to_html(),
        'purchase': purchase_df.to_html()
    }
    return render(request, 'products/main.html', context)

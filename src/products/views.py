from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
# Create your views here.


def chart_select_view(request):
    error_message=None
    df = None

    qs = Product.objects.all().values()
    qs2 = Purchase.objects.all().values()
    product_df = pd.DataFrame(qs)
    purchase_df = pd.DataFrame(qs2)
    product_df['product_id'] = product_df['id']

    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'created_dt_y'], axis=1).rename({'id_x': 'id', 'created_dt_x': 'created_dt'}, axis=1)

        if request.method == 'POST':
            chart_type = request.POST['sales']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']

            df['created_dt'] = df['created_dt'].apply(lambda x: x.strftime('%y-%m-%d'))
            df2 = df.groupby('created_dt', as_index=False)['total_price'].agg('sum')

            if chart_type != '':
                if date_from != '' and date_to !='':
                    df = df[(df['data']> date_from) & (df['date']<date_to)]
                    df2 = df.groupby('created_dt', as_index=False)['total_price'].agg('sum')
                # get a graph
                
            else:
                error_message = 'Please select a chart type to continue'
    else:
        error_message = 'No records in the database',

    context = {
        'error_message': error_message
    }
    return render(request, 'products/main.html', context)

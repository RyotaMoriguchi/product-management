from django.shortcuts import render

# Create your views here.
def product_list(request):
    """商品一覧"""
    return render(request,
                  'product_list.html')
from django.shortcuts import render, get_object_or_404
from .models import Item
from .form import ItemForm


def index(request):
    Items = Item.objects.all()
    return render(request, "index.html", locals())


def itemsdetail(request, IID):
    item = get_object_or_404(Item, pk=IID)
    return render(request, 'itemsdetail.html', locals())


def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            ItemName = form.cleaned_data.get('Name')
            Price = form.cleaned_data.get('Price')
            Description = form.cleaned_data.get('Description')
            Type = form.cleaned_data.get('Type')
            TradingLocation = form.cleaned_data.get('TradingLocation')
            item = Item.object.create(ItemName=ItemName, Price=Price, Description=Description
                                      , Type=Type, TradingLocation=TradingLocation)
            item.save()
        else:
            message = 'Wrong!'
    else:
        form = ItemForm()
    return render(request, 'additem.html', locals())


def edit(request, IID):
    item = get_object_or_404(Item, pk=IID)
    if item.Seller == request.user:
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                ItemName = form.cleaned_data.get('Name')
                Price = form.cleaned_data.get('Price')
                Description = form.cleaned_data.get('Description')
                Type = form.cleaned_data.get('Type')
                TradingLocation = form.cleaned_data.get('TradingLocation')

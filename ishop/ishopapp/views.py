from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .form import ItemForm
from django.contrib.auth.decorators import login_required


def index(request):
    Items = Item.objects.filter(Status=False)
    return render(request, "index.html", locals())


def itemsdetail(request, IID):
    item = get_object_or_404(Item, pk=IID)
    return render(request, 'itemsdetail.html', locals())

@login_required(login_url="/ishop/login/")
def additem(request):
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            Name = itemform.cleaned_data['Name']
            Price = itemform.cleaned_data['Price']
            Description = itemform.cleaned_data['Description']
            Type = itemform.cleaned_data['Type']
            TradingLocation = itemform.cleaned_data['TradingLocation']
            Seller = request.user
            item = Item.objects.create(Name=Name, Price=Price, Description=Description, Type=Type, TradingLocation=TradingLocation, Seller=request.user)
            message = 'Item added!'
        else:
            message = 'The inputs maybe invalid!'
    else:
        message = 'All information should be inputed!'
        itemform = ItemForm()
    return render(request, "additem.html", locals())


@login_required(login_url="/ishop/login/")
def edititem(request, IID):
    item = Item.objects.get(IID=IID)
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            #for key, value in ItemForm.cleaned_data.items():
                #if value == '':
                    #ItemForm.cleaned_data[key] = item.__dict__[key]
                #else:
                    #ItemForm.cleaned_data[key] = value

            item.Name = itemform.cleaned_data['Name']
            item.Price = itemform.cleaned_data['Price']
            item.Description = itemform.cleaned_data['Description']
            item.Type = itemform.cleaned_data['Type']
            item.TradingLocation = itemform.cleaned_data['TradingLocation']
            item.Status = itemform.cleaned_data['Status']
            Seller = request.user
            item.save()
            message = 'Item edited!'
        else:
            message = 'The inputs maybe invalid!'
    else:
        message = 'All information should be inputed!'
        itemform = ItemForm()
    return render(request, "edititem.html", locals())

@login_required(login_url="/ishop/login/")
def myitem(request):
    Items = Item.objects.filter(Seller=request.user, Status=False)
    return render(request, "myitem.html", locals())


@login_required(login_url="/ishop/login/")
def myitemsdetail(request, IID):
    item = get_object_or_404(Item, pk=IID)
    return render(request, 'myitemsdetail.html', locals())

#f



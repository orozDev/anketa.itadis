from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import *


def main(request):
    context = {
        'forms': Forms.objects.filter(is_published=True)
    }

    return render(request, 'main.html', context)


def getForm(request, pk):
    if request.method == 'POST':

        form = Forms.objects.get(id=pk)
        time = timezone.localdate()
        data = Datas.objects.create(
            name=f'{form.title}_{time}',
            form=form
        )

        for item in form.inputs.all():
            temp = f'{item.type_of_input.title }_{item.id}' 
            value = request.POST.get(temp, None)

            if value == '':
                value = None

            if item.type_of_input.title == 'file':
                try:
                    value = request.FILES[temp]
                    fs = FileSystemStorage('media/files/')
                    fs.save(value.name, value) 
                    value = f'/media/files/{value.name}'
                except Exception:
                    pass
            
            DetailDatas.objects.create(
                item=value,
                data=data,
                input_type=item
            )
        
        messages.success(request, '')
        return redirect('/')


    context = {
        'form': get_object_or_404(Forms, id=pk, is_published=True)
    }

    return render(request, 'item_form.html', context)


@login_required(login_url='/login')
def adminPanel(request):
    context = {
        'forms': Forms.objects.annotate(cnt=Count('datas'))
    }

    return render(request, 'simple_admin/admin_panel.html', context)


@login_required(login_url='/login')
def listDatas(request, pk):

    if request.method == 'POST':
        form = Forms.objects.get(id=pk)
        if form.is_published: 
            form.is_published = False
        else:
            form.is_published = True
        form.save()

        return JsonResponse({'is_done': True})

    context = {
        'datas': Datas.objects.filter(form__id=pk).order_by('-created_at'),
        'form': Forms.objects.get(id=pk),
    }

    return render(request, 'simple_admin/list_of_datas.html', context)


@login_required(login_url='/login')
def getData(request, pk):
    context = {
        'data': Datas.objects.get(id=pk),
        'detailDatas': DetailDatas.objects.filter(data__id=pk),
    }

    return render(request, 'simple_admin/item_of_data.html', context)
    

@login_required(login_url='/login')
def deleteForm(request, pk):
    if request.user.is_superuser:
        form = Forms.objects.get(id=pk)
        form.inputs.all().delete()
        form.delete()
        messages.success(request, f'Форма успешно удалена!')

    return redirect('/admin/')


@login_required(login_url='/login')
def search_datas(request):
    title = request.GET.get('search')
    context = {
        'detailDatas': DetailDatas.objects.filter(item__icontains=title),
        'title': title,
    }

    return render(request, 'simple_admin/search.html', context)


def login_profile(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(request.session['next_link'])
            
            messages.error(request, f'Не существует пользователя или неверный пароль!')
            return render(request, 'login.html', {})
        
        request.session['next_link'] = request.GET.get('next')
        return render(request, 'login.html', {})
    return redirect('/')


@login_required(login_url='/login')
def changeCheckerOfData(request):
    pk = request.GET.get('pk', None)
    if pk is not None:
        data = Datas.objects.get(id=pk)
        if data.is_checked:
            data.is_checked = False
        else:
            data.is_checked = True
        data.save()

        return JsonResponse({'is_done': True})
    return JsonResponse({'is_done': False})


@login_required(login_url='/login')
def deleteData(request, pk):
    data = Datas.objects.get(id=pk)
    id = data.form.id
    if request.user.is_superuser:
        DetailDatas.objects.filter(data=data).delete()
        data.delete()
        messages.success(request, f'Запись успешно удалена!')

    return redirect(f'/admin/list_datas/{id}/')



@login_required(login_url='login/')
def addForm(request):
    context = {
        'types': Types_of_input.objects.all(),
    }

    return render(request, 'simple_admin/addForm.html', context)


@login_required(login_url='login/')
def logout_profile(request):
    logout(request)
    return redirect('/')
    
# Create your views here.

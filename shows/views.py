import hashlib
import os
from django.shortcuts import get_object_or_404, redirect, render

from shows.models import Show

def INDEX(request):
    shows = Show.objects.all()

    context = {
        'shows':shows,
    }
    return render(request,'index.html',context)


def ADD(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        tipo = request.POST.get('tipo')
        assentos = request.POST.get('assentos')
        elenco = request.POST.get('elenco')
        secoes = request.POST.get('secoes')
        data = request.POST.get('data')
        horarios = request.POST.get('horarios')
        imagem = request.FILES.get('imagem')
  
        if(int(secoes) < 0 or int(secoes) > 5 or int(assentos) < 0 or int(assentos) > 50):
            return render(request,'index.html')
    
        shows = Show(
            nome = nome,
            descricao = descricao,
            preco = preco,
            tipo = tipo,
            assentos = assentos,
            elenco = elenco,
            secoes = secoes,
            data = data,
            horarios = horarios,
            imagem = imagem
        )
        shows.save()
        return redirect('shows')
    
    return render(request,'index.html')


def UPDATE(request, id):
    show = get_object_or_404(Show, pk=id)
    old_image_path = show.imagem.path if show.imagem else None

    if request.method == "POST":
        # Atualize os campos do show
        show.nome = request.POST.get('nome')
        show.descricao = request.POST.get('descricao')
        show.preco = request.POST.get('preco')
        show.tipo = request.POST.get('tipo')
        show.assentos = request.POST.get('assentos')
        show.elenco = request.POST.get('elenco')
        show.secoes = request.POST.get('secoes')
        show.data = request.POST.get('data')
        show.horarios = request.POST.get('horarios')

        if(int(show.secoes) < 0 or int(show.secoes) > 5 or int(show.assentos) < 0 or int(show.assentos) > 50):
            return render(request,'index.html')
        
        # Verifique se uma nova imagem foi carregada
        if 'imagem' in request.FILES:
            new_image = request.FILES['imagem']
            new_image_hash = hashlib.md5(new_image.read()).hexdigest()

            # Verifique se a nova imagem é diferente da imagem existente
            if old_image_path:
                with open(old_image_path, 'rb') as f:
                    old_image_hash = hashlib.md5(f.read()).hexdigest()
                
                if new_image_hash != old_image_hash:
                    show.imagem = new_image
                    # Se existir uma imagem antiga, remova-a
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)
            else:
                show.imagem = new_image

        show.save()
        return redirect('shows')

    return render(request, 'index.html')
def DELETE(request, id):
    Show.objects.filter(id=id).delete()
    return redirect('shows')



import hashlib
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import default_storage
from shows.models import Show
from django.utils.text import slugify
import uuid

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
  
        if int(secoes) < 0 or int(secoes) > 5 or int(assentos) < 0 or int(assentos) > 50:
            return render(request, 'index.html')
    
        shows = Show(
            nome=nome,
            descricao=descricao,
            preco=preco,
            tipo=tipo,
            assentos=assentos,
            elenco=elenco,
            secoes=secoes,
            data=data,
            horarios=horarios,
            imagem=imagem
        )

        # Verificar e alterar o nome da imagem se já existir
        if imagem:
            nome_imagem = imagem.name
            nome_base, nome_extensao = os.path.splitext(nome_imagem)
            novo_nome = f"{slugify(nome_base)}_{uuid.uuid4().hex}{nome_extensao}"
            
            # Garantir que o novo nome não exista no armazenamento
            while default_storage.exists(novo_nome):
                novo_nome = f"{slugify(nome_base)}_{uuid.uuid4().hex}{nome_extensao}"
            
            # Atribuir o novo nome à imagem do objeto Show
            shows.imagem.name = novo_nome

        shows.save()
        return redirect('shows')
    
    return render(request, 'index.html')

def UPDATE(request, id):
    show = get_object_or_404(Show, pk=id)
    old_image_name = show.imagem.name if show.imagem else None

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

        if int(show.secoes) < 0 or int(show.secoes) > 5 or int(show.assentos) < 0 or int(show.assentos) > 50:
            return render(request, 'index.html')

        # Verifique se uma nova imagem foi carregada
        if 'imagem' in request.FILES:
            new_image = request.FILES['imagem']

            # Gerar um novo nome único para a nova imagem
            nome_imagem = new_image.name
            nome_base, nome_extensao = os.path.splitext(nome_imagem)
            novo_nome = f"shows/{slugify(nome_base)}_{uuid.uuid4().hex}{nome_extensao}"  # Nome com a pasta shows/

            # Salvar a nova imagem usando default_storage
            new_image_path = default_storage.save(novo_nome, new_image)

            # Atualizar a propriedade imagem do objeto Show
            show.imagem.name = new_image_path

            # Se existir uma imagem antiga, remova-a
            if old_image_name:
                default_storage.delete(old_image_name)

        show.save()
        return redirect('shows')

    return render(request, 'index.html')

def DELETE(request, id):
    show = get_object_or_404(Show, id=id)
    if show.imagem and default_storage.exists(show.imagem.name):
        default_storage.delete(show.imagem.name)  # Deleta o arquivo de mídia do Google Cloud Storage
    show.delete()
    return redirect('shows')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  MyUserCreationForm
from django.contrib.auth import logout as user_logout
#from .models import Carro, Aluguel,Cliente
#from .forms import AluguelForm,CarroForm


def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'pages/contato.html')

def index2(request):
    return render(request, 'index2.html')

def visu(request):
    return render(request, 'visu.html')

def base(request):
    return render(request, 'base.html')

def alugueis(request):
    
    return render(request, 'alugueis.html')

def login_view(request):
    if request.method == 'GET':
      return render(request, template_name='login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('visu')
        else:
            # Tratar o erro de autenticação aqui
            return render(request, 'login', {'error_message': 'Nome de usuário ou senha inválido.'})
    else:
        return render(request, 'visu')
    
def registration(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visu')
        else:
            form = MyUserCreationForm()
            return render(request, "login.html", {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, "registration.html", {'form': form})
    
def logout(request):
    user_logout(request)
    return redirect('index')


#def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros":carros})

#def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'carro/detalhar.html', {"carro":carro})

#def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarroForm()
            return render(request, "carro/cadastrar.html" , {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastrar.html", {'form': form})

#def atualizar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    form = CarroForm(instance=carro)
    
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "carro/atualizar.html", {'form': form})
    else:
        return render(request, "carro/atualizar.html", {'form': form})
    
#def deletar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)

    if carro:
        carro.delete()
        return redirect("/")
    else:
        return render(request, "carro/listar.html", {'msg': "carro não encontrado"})


#def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar.html', {"clientes":clientes})

#def detalhar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'cliente/detalhar.html', {"cliente":cliente})

#def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'aluguel/listar.html', {"alugueis":alugueis})

    


#def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

#def realizar_aluguel_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    aluguel = Aluguel()
    aluguel.carro = carro
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})
    


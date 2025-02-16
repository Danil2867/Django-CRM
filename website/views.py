from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
	#Проверка на аутентификацию пользователя
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Вход в аккаунт
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Вы успешно зашли в аккаунт!")
			return redirect('home')
		else:
			messages.success(request, "Произошла ошибка, Попробуйте ещё раз!")
			return redirect('home')
	else:			
		return render(request, 'home.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "Вы успешно вышли из аккаунта")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})
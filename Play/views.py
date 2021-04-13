import logging
import operator

from django.shortcuts import render


from nltk.corpus import sentiwordnet as swn
import itertools

from nltk.corpus import sentiwordnet as swn

import json

from django.http import HttpResponse

from .forms import FormularioSolucion
from .models import solucion 



def inicio(request):

	context = {

		'form':FormularioSolucion()

	}

	return render(request, 'inicio.html', context)


def CrearSolucion(request):

	if request.method == 'POST':

		length = request.POST.get('length')
		letras =request.POST.get('letters')
		print(letras)

		
		f = open("combinations.txt", 'w')
		k = list(itertools.permutations(letras, int(length)))

		for i in k:
			for l in i:
				f.write(l)
			f.write('\n')
		f.close()


		h = []
		with open('combinations.txt') as hai:
			h = [word.lower().strip() for word in hai]


		dicionario = {}
		for o in h:
			if o not in dicionario:
				dicionario[o] = 0
			else:
				dicionario[o] +=1


		lista = []

		for l in dicionario:
			v = list(swn.senti_synsets(l))
			if v:
				lista.append(l)

		print(lista)

		datos = {}

		datos['length'] =length
		datos['palabras']=letras
		datos['lista'] = lista

		return HttpResponse(

			json.dumps(datos),
			content_type ='application/json'
		)

	else:
		return HttpResponse(

			json.dumps({'error':'error'}),
			content_type ='application/json'
		)
	
	
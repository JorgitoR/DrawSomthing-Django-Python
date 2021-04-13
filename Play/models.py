from django.db import models



class solucion(models.Model):

	length = models.IntegerField()
	letras = models.CharField(max_length=20)


	def __str__(self):
		return self.letras
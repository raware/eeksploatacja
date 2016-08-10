from django.db import models



class Zjazd(models.Model):

	nr_motorniczego = models.CharField(max_length=8, null=True)
	linia_brygada = models.CharField(max_length=8, null=True)
	nr_tramwaju = models.CharField(max_length=8)
	opis_usterki = models.TextField()
	data = models.DateField(auto_now_add=True, blank=True)
	godzina = models.TimeField(auto_now_add=True, blank=True)
	symbol = models.CharField(max_length=8, null=True)
	opis_naprawy = models.TextField(null=True)
	kto_naprawil = models.CharField(max_length=200, null=True)

	class Meta:
		verbose_name = ('Zjazd techniczny')
		verbose_name_plural = ('Zjazdy techniczne')

	def tytul(self):
		if self.data == None or self.godzina == None:
			return self.nr_tramwaju
		tytul = self.nr_tramwaju+' '+str(self.data.strftime('%d-%m-%Y'))+' '+str(self.godzina.strftime('%H:%M'))
		return tytul

	def dodaj(self):
		self.save()

	def __str__(self):
		return self.tytul()

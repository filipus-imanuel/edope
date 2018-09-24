from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Berkas(models.Model):
	nama = models.CharField(verbose_name="Nama Berkas", max_length=100)
	berkas = models.FileField(verbose_name="Berkas", upload_to='media/uploads/')
	keterangan = models.CharField(verbose_name="Keterangan Berkas", max_length=255, blank=True, null=True)
	upload_by = models.ForeignKey(User, verbose_name="Diupload oleh", on_delete=models.PROTECT)

	def __str__(self):
		return (str(self.id)+". "+self.nama)

	class Meta:
		verbose_name = 'Data Berkas'
		verbose_name_plural = "Data Berkas"
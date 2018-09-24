from django.contrib import admin
from dokumen.models import Berkas

# Register your models here.

class BerkasAdmin(admin.ModelAdmin):
	list_display = ('nama', 'keterangan')
	# exclude = ('keterangan',)

admin.site.register(Berkas, BerkasAdmin)
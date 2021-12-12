from django.contrib import admin
from . import models
# Register your models here.

class BaseForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class FornecedoresForm(BaseForm):
    search_fields = ['razao_social','cnpj','email','telefone']
    list_filter = ['razao_social']


admin.site.register(models.Fornecedores, FornecedoresForm)
admin.site.register(models.NaturezasDespesa)
admin.site.register(models.Marcas,BaseForm)
admin.site.register(models.Bens,BaseForm)
admin.site.register(models.Notas_fiscais,BaseForm)
admin.site.register(models.ItensNotaFiscal,BaseForm)
admin.site.register(models.SituacoesUsoBem)
admin.site.register(models.EstadoBem)




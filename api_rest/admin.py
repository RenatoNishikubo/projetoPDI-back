from django.contrib import admin

from .models import User, Declarante, Dependente, Propriedade, Endereco

admin.site.register(User)
admin.site.register(Declarante)
admin.site.register(Dependente)
admin.site.register(Propriedade)
admin.site.register(Endereco)
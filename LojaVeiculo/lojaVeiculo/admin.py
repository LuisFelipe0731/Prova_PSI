from django.contrib import admin #isso já vai estar existindo no
# Register your models here.
from .models import * #imporata nossos models
admin.site.register(Veiculo) #adiciona a interface do adm

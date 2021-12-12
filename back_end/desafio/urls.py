"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from patrimonio import views
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from django.conf.urls.static import static
from django.conf.urls import url
from desafio import settings
from rest_framework.documentation import include_docs_urls

from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'fornecedores', views.FornecedoresView)
router.register(r'notas', views.Notas_fiscaisView)
router.register(r'bens', views.BensView)
router.register(r'naturezas', views.NaturezasDespesaView)
router.register(r'itensnotas', views.ItensNotaFiscalView)


urlpatterns = [
    path('api/auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api/token/', obtain_jwt_token),
    path('api/refresh-token/', refresh_jwt_token),
    path('', include(router.urls)),
    
    path('admin/', admin.site.urls),
    path('swagger/', include_docs_urls(title='API Documentation',
                                                    description='Documentação dos endpoints',
                                                    ), name='api-docs'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


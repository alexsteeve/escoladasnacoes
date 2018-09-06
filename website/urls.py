from website.views import IndexTemplateView,  \
     EstudanteListView, EstudanteCreateView, EstudanteUpdateView , EstudanteDeleteView, AniversariantesListView, \
     EstudantePerfilView, CursoListView, CursoPerfilView, CursoPeriodoView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /estudante/cadastrar
    path('estudante/cadastrar', EstudanteCreateView.as_view(), name="cadastra_estudante"),

    # GET /estudantes
    path('estudantes/', EstudanteListView.as_view(), name="lista_estudantes"),

    # GET /estudantes
    path('aniversariantes/', AniversariantesListView.as_view(), name="lista_aniversariantes"),

    # GET/POST /estudante/{pk}
    path('estudante/<pk>', EstudanteUpdateView.as_view(), name="atualiza_estudante"),

    # GET/POST /estudantes/excluir/{pk}
    path('estudante/excluir/<pk>', EstudanteDeleteView.as_view(), name="deleta_estudante"),

    # GET /estudantes/perfil/{pk}
    path('estudante/perfil/<pk>', EstudantePerfilView.as_view(), name="perfil_estudante"),

    # GET /cursos
    path('cursos/', CursoListView.as_view(), name="lista_cursos"),

    # GET /cursos/perfil/{pk}
    path('curso/perfil/<pk>', CursoPerfilView.as_view(), name="perfil_curso"),

    # GET /cursos/periodo/perfil/{pk}
    path('curso/periodo/perfil/<pk>', CursoPeriodoView.as_view(), name="periodo_curso"),

]

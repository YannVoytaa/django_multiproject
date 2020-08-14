from django.urls import path
from home import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:number>',views.project,name='project'),
    path('1/<int:row>/<int:col>',views.TIC_TAC_TOE.tic_tac_toe,name='tic_tac_toe')
]
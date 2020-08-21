from django.urls import path
from home import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:number>',views.project,name='project'),
    path('1/<int:row>/<int:col>',views.TIC_TAC_TOE.tic_tac_toe,name='tic_tac_toe'),
    path('2/<int:nr>',views.ROCK_PAPER_SCISSORS.rock_paper_scissors,name='rock_paper_scissors'),
    path('3/register',views.CLICKER.register,name='clicker_register'),
    path('3/login',views.CLICKER.login,name='clicker_login'),
    path('3/logout',views.CLICKER.logout,name='clicker_logout'),
    path('3/get',views.CLICKER.get,name='clicker_get'),
]
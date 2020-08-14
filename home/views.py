from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
NUM_OF_PROJECTS=7
# Create your views here.
def home(request):
    context={
        'no_of_projects':[x for x in range(1,NUM_OF_PROJECTS+1)],
    }
    return render(request,'home/index.html',context=context)
class Switcher():
    def trigger(self,nr,request):
        method_name='f'+nr
        method=getattr(self,method_name,'RIP')
        return method(request)
    def f1(self,request):
        return TIC_TAC_TOE.play(request)
    def f2(self,request):
        return render(request,'home/2.html')

def project(request,number):
    return SWITCHER.trigger(str(number),request)

class Tic_Tac_Toe():
    def __init__(self):
        self.grid=[['0' for x in range(3)] for y in range(3)]
        self.turn=0
        self.context = {
            'grid': self.grid,
        }
    def play(self,request):
        return render(request,'home/1.html',context=self.context)
    def tic_tac_toe(self,request,row,col):
        global TIC_TAC_TOE
        if row==0:
            self.grid=[['0' for x in range(3)] for y in range(3)]
            self.turn = 0
            self.context={
                'grid':self.grid,
            }
            return HttpResponseRedirect(reverse('project',args=[1]))
        self.grid[row-1][col-1]=self.turn
        self.turn=1-self.turn
        return HttpResponseRedirect(reverse('project',args=[1]))
SWITCHER=Switcher()
TIC_TAC_TOE=Tic_Tac_Toe()
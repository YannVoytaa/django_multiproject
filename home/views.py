from copy import deepcopy

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
NUM_OF_PROJECTS=7
# Create your views here.
def home(request):
    context={
        'no_of_projects':[x for x in range(1,NUM_OF_PROJECTS+1)],
    }
    TIC_TAC_TOE.tic_tac_toe(request,0,0)
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

BASIC_GRID=[['' for x in range(3)] for y in range(3)]
MAPPED={
    0:'O',
    1:'X',
}
class Tic_Tac_Toe():
    def __init__(self):
        self.grid=deepcopy(BASIC_GRID)
        self.turn=0
        self.context = {
            'grid': self.grid,
            'extras':[],
        }
    def play(self,request):
        self.context['extras'].append('Move: Player '+str(self.turn+1))
        return render(request,'home/1.html',context=self.context)
    def check(self):
        if self.grid[0][0]==self.grid[0][1]==self.grid[0][2]!='':
            return True
        if self.grid[1][0]==self.grid[1][1]==self.grid[1][2]!='':
            return True
        if self.grid[2][0]==self.grid[2][1]==self.grid[2][2]!='':
            return True
        if self.grid[0][0]==self.grid[1][0]==self.grid[2][0]!='':
            return True
        if self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != '':
            return True
        if self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != '':
            return True
        if self.grid[0][0]==self.grid[1][1]==self.grid[2][2]!='':
            return True
        if self.grid[0][2]==self.grid[1][1]==self.grid[2][0]!='':
            return True
    def tic_tac_toe(self,request,row,col):
        global TIC_TAC_TOE
        self.context['extras']=[]
        if row==0:
            self.grid=deepcopy(BASIC_GRID)
            self.turn = 0
            self.context={
                'grid':self.grid,
                'extras':[],
            }
            return HttpResponseRedirect(reverse('project',args=[1]))
        if self.grid[row-1][col-1]=='' and not self.check():
            self.grid[row-1][col-1]=MAPPED[self.turn]
            if self.check():
                self.context['extras'].append('Player ' + str(self.turn + 1)+' Won!')
                return HttpResponseRedirect(reverse('project', args=[1]))
            self.turn=1-self.turn
        return HttpResponseRedirect(reverse('project',args=[1]))
SWITCHER=Switcher()
TIC_TAC_TOE=Tic_Tac_Toe()
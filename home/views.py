from copy import deepcopy
import random
from math import floor

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from .models import Clicker_User
NUM_OF_PROJECTS=7
# Create your views here.
def home(request):
    context_list=[
        {'name':'Tic Tac Toe','href':1},
        {'name': 'Rock Paper Scissors', 'href': 2},
        {'name': 'Clicker', 'href': 3},
        {'name':'Bfs','href':4}
    ]
    for x in range(len(context_list)+1,NUM_OF_PROJECTS+1):
        context_list.append({'name':'Project '+str(x),'href':x})
    context={
        'no_of_projects':context_list,
    }
    TIC_TAC_TOE.tic_tac_toe(request,0,0)
    ROCK_PAPER_SCISSORS.__init__()
    BFS.__init__()
    return render(request,'home/index.html',context=context)
class Switcher():
    def trigger(self,nr,request):
        method_name='f'+nr
        method=getattr(self,method_name,'RIP')
        return method(request)
    def f1(self,request):
        return TIC_TAC_TOE.play(request)
    def f2(self,request):
        return ROCK_PAPER_SCISSORS.play(request)
    def f3(self,request):
        return CLICKER.play(request)
    def f4(self,request):
        return BFS.play(request)
def project(request,number):
    return SWITCHER.trigger(str(number),request)

BASIC_GRID=[['' for x in range(3)] for y in range(3)]
TTT_MAPPED={
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
        if len(self.context['extras'])>0 and self.context['extras'][0].startswith("Player"):
            pass
        else:
            self.context['extras']=[]
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
            self.grid[row-1][col-1]=TTT_MAPPED[self.turn]
            if self.check():
                self.context['extras'].append('Player ' + str(self.turn + 1)+' Won!')
                return HttpResponseRedirect(reverse('project', args=[1]))
            self.turn=1-self.turn
        return HttpResponseRedirect(reverse('project',args=[1]))

RPS_MAPPED={
    0:'Rock',
    1:'Paper',
    2:'Scissors',
}
class Rock_Paper_Scissors():
    def __init__(self):
        self.choice=0
        self.context={}
    def play(self,request):
        return render(request,'home/2.html',context=self.context)
    def rock_paper_scissors(self,request,nr):
        self.choice = floor(random.random() * 3)
        self.context = {'enemy':'Enemy chose '+RPS_MAPPED[self.choice]}
        if nr==self.choice:
            self.context['winner']="It's a draw"
        elif nr==self.choice+1 or nr+2==self.choice:
            self.context['winner']="You won"
        else:
            self.context['winner']="You lost"
        return HttpResponseRedirect(reverse('project',args=[2]))


class Clicker():
    def __init__(self):
        self.user=None
        self.context={'user':self.user}
    def play(self,request):
        return render(request,'home/3.html',context=self.context)
    def register(self,request):
        potential=Clicker_User.objects.filter(username=request.POST['login'])
        if len(potential)==0:
            new_user=Clicker_User(username=request.POST['login'],password=request.POST['password'],money=0)
            new_user.save()
            self.user=new_user
            self.context['user']=self.user
            self.context['logged_in']={'money':new_user.money}
        else:
            self.context['extra']=True
        return HttpResponseRedirect(reverse('project',args=[3]))
    def login(self,request):
        self.user=get_object_or_404(Clicker_User,username=request.POST['login'],password=request.POST['password'])
        self.user.money+=1
        self.user.save()
        self.context['user'] = self.user
        self.context['logged_in']={'money':self.user.money}
        return HttpResponseRedirect(reverse('project', args=[3]))
    def logout(self,request):
        self.user=None
        self.context={}
        return HttpResponseRedirect(reverse('project', args=[3]))
    def get(self,request):
        self.user.money+=1
        self.user.save()
        self.context['logged_in'] = {'money': self.user.money}
        return HttpResponseRedirect(reverse('project', args=[3]))

class Bfs():
    def __init__(self):
        self.size=10
        grid=[]
        for x in range(self.size):
            row=[]
            for y in range(self.size):
                r=random.random()
                if r<0.1:
                    row.append(1)
                else:
                    row.append(0)
            grid.append(deepcopy(row))
        self.dist=[[None for x in range(self.size)] for y in range(self.size)]
        start,end=(floor(random.random()*self.size),floor(random.random()*self.size)),(floor(random.random()*self.size),floor(random.random()*self.size))
        while start==end:
            end = (floor(random.random() * self.size), floor(random.random() * self.size))
        grid[start[0]][start[1]]=2
        grid[end[0]][end[1]]=3
        self.start,self.end=start,end
        self.grid=[]
        for x in range(self.size):
            row=[]
            for y in range(self.size):
                row.append([grid[x][y],self.dist[x][y]])
            self.grid.append(deepcopy(row))
        self.context={
            'grid':self.grid,
        }
    def play(self,request):
        return render(request,'home/4.html',context=self.context)
    def randomize(self,request):
        self.__init__()
        return HttpResponseRedirect(reverse('project',args=[4]))
    def simulate(self,request):
        q=[]
        q.append(self.start)
        self.dist=[[None for x in range(self.size)] for y in range(self.size)]
        self.dist[self.start[0]][self.start[1]]=0
        while len(q)>0:
            akt=q[0]
            q=q[1:]
            if akt[1]-1>=0 and self.dist[akt[0]][akt[1]-1]==None and self.grid[akt[0]][akt[1]-1][0]!=1:
                self.dist[akt[0]][akt[1]-1]=self.dist[akt[0]][akt[1]]+1
                q.append((akt[0],akt[1]-1))
            if akt[0]-1>=0 and self.dist[akt[0]-1][akt[1]]==None and self.grid[akt[0]-1][akt[1]][0]!=1:
                self.dist[akt[0]-1][akt[1]]=self.dist[akt[0]][akt[1]]+1
                q.append((akt[0]-1, akt[1]))
            if akt[1]+1<self.size and self.dist[akt[0]][akt[1]+1]==None and self.grid[akt[0]][akt[1]+1][0]!=1:
                self.dist[akt[0]][akt[1]+1]=self.dist[akt[0]][akt[1]]+1
                q.append((akt[0], akt[1] + 1))
            if akt[0]+1<self.size and self.dist[akt[0]+1][akt[1]]==None and self.grid[akt[0]+1][akt[1]][0]!=1:
                self.dist[akt[0]+1][akt[1]]=self.dist[akt[0]][akt[1]]+1
                q.append((akt[0]+1, akt[1]))
        newgrid = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append([self.grid[x][y][0], self.dist[x][y]])
            newgrid.append(deepcopy(row))
        self.grid=deepcopy(newgrid)
        self.context = {
            'grid': self.grid,
        }
        return HttpResponseRedirect(reverse('project',args=[4]))
SWITCHER=Switcher()
TIC_TAC_TOE=Tic_Tac_Toe()
ROCK_PAPER_SCISSORS=Rock_Paper_Scissors()
CLICKER=Clicker()
BFS=Bfs()
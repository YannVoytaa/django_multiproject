let player=1;
let signs=['','O','X'];
let button=new Array(5);
let counter=0
let move_p=document.getElementById('move');
function check(){
    for(let x=1;x<=3;x++){

    if (button[x][1].textContent===button[x][2].textContent && button[x][2].textContent===button[x][3].textContent && button[x][1].textContent)return true;
    if (button[1][x].textContent===button[2][x].textContent && button[2][x].textContent===button[3][x].textContent && button[3][x].textContent)return true;
    if (button[1][1].textContent===button[2][2].textContent && button[2][2].textContent===button[3][3].textContent && button[1][1].textContent)return true;
    if (button[3][1].textContent===button[2][2].textContent && button[2][2].textContent===button[1][3].textContent && button[3][1].textContent)return true;
    }
    return false;
}
function btnClick(){
    counter++;
    this.textContent=signs[player];
    if(check()){
        move_p.innerHTML='Player '+player.toString()+' Won!';
        alert('Player '+player.toString()+' Won!');
        for(let x=1;x<=3;x++){
            for(let y=1;y<=3;y++){
                button[x][y].removeEventListener('click',btnClick);
            }
        }
    }
    else{
        player=3-player;
        move_p.innerHTML='Move: Player '+player.toString();
        if(counter===9){
            alert("It's a draw!");
            move_p.innerHTML="It's a draw!";
        }
    }
    this.removeEventListener('click',btnClick);
}
function main(){
    for(let x=1;x<=3;x++){
        button[x]=new Array(5);
    }
    for(let x=1;x<=3;x++){
        for(let y=1;y<=3;y++){
            button[x][y]=document.getElementById('button'+x.toString()+y.toString());
            button[x][y].textContent='';
            button[x][y].addEventListener('click',btnClick);
        }
    }

}

main();
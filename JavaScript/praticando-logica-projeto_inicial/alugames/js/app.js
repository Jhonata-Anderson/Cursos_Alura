let alugados = 1;

function alterarStatus(id) {
    let gameClicado = document.getElementById(`game-${id}`);
    let imagem = gameClicado.querySelector('.dashboard__item__img');
    let botao = gameClicado.querySelector('.dashboard__item__button');
    
    if (imagem.classList.contains('dashboard__item__img--rented')) {
        let confirmarDevoluçao = confirm('Deseja realmente estar devolvendo este jogo?');
        if (confirmarDevoluçao){
            imagem.classList.remove('dashboard__item__img--rented');
            botao.classList.remove('dashboard__item__button--return');
            botao.textContent = 'Alugar';
        }
    } else {
            imagem.classList.add('dashboard__item__img--rented');
            botao.classList.add('dashboard__item__button--return');
            botao.textContent = 'Devolver';
            contadorDeJogosAlugados();
        }
}

function contadorDeJogosAlugados(){
    alugados ++;
    console.log(alugados);
}
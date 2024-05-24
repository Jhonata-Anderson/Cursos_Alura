let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function botaoConsole() {
    console.log('O botão foi clicado');
}

function botaoAlerta() {
    console.log('Eu amo JS');
}

function botaoPrompt() {
    let cidade = prompt('Digite um nome de uma cidade do Brasil!');
    alert (`Estive em ${cidade} e lembrei de você.`);
}

function botaoSoma() {
    let numero1 = parseInt(prompt('Digite um número'));
    let numero2 = parseInt(prompt('Digite outro número'));
    let soma = (numero1 + numero2);
    alert (`A soma de ${numero1} e ${numero2} é igual a ${soma}`);
}
let totalGeral = 0;
limpar();

function adicionar() {
    //recuperar valores: nome do produto, quantidade e valor;
    let produto = document.getElementById('produto').value;
    let nomeProduto = produto.split('-')[0];
    let valorUnitario = produto.split('R$')[1];
    let quantidade = document.getElementById('quantidade').value;
    //calcular o preço, o nosso subtotal;
    let preço = (quantidade * valorUnitario);
    //adicionar no carrinho;
    if (quantidade <= 0){
        alert('Quantidade inserida inválida, o número inserido precisa ser maior que 0!');
    } else {
        let carrinho = document.getElementById('lista-produtos');
        carrinho.innerHTML = carrinho.innerHTML + `<section class="carrinho__produtos__produto">
          <span class="texto-azul">${quantidade}x</span> ${nomeProduto} <span class="texto-azul">R$${preço}</span>
        </section>`;
    }
    //atualizar o grande total;
    totalGeral = totalGeral + preço;
    let valorTotal = document.getElementById('valor-total');
    valorTotal.innerHTML = `<span class="texto-azul" id="valor-total">R$ ${totalGeral}</span>`
    document.getElementById('quantidade').value = 0;
};

function limpar() {
    document.getElementById('lista-produtos').innerHTML = '';
    let valorTotal = document.getElementById('valor-total');
    valorTotal.innerHTML = `<span class="texto-azul" id="valor-total">R$ 0</span>`
};
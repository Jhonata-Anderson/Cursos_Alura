function comprar(){
    // pegando os valores
    let tipoIngresso = document.getElementById('tipo-ingresso').value;
    let quantidade = document.getElementById('qtd').value;
    let quantidadePista = document.getElementById('qtd-pista');
    let quantidadeSuperior = document.getElementById('qtd-superior');
    let quantidadeInferior =document.getElementById('qtd-inferior');
    // Calcular o restante dos ingressos e mostrar eles
    if (tipoIngresso == 'inferior'){
        let restanteInferior = (quantidadeInferior.textContent) - quantidade;
        if (quantidade <= 0){
            alert('Quantidade inválido, o número inserido precisa ser maior do que 0!')
        } else{
            if (restanteInferior < 0) {
                alert('Quantidade indisponível para cadeira inferior!');
            } else{
                quantidadeInferior.innerHTML = (`${restanteInferior}`);
                alert('Compra realizada com sucesso!'); 
            }
        }
    } else if (tipoIngresso == 'superior'){
        let restanteSuperior = (quantidadeSuperior.textContent) - quantidade;
        if (restanteSuperior < 0) {
            alert('Quantidade indisponível para cadeira superior!');
        } else{
            quantidadeSuperior.innerHTML = (`${restanteSuperior}`); 
            alert('Compra realizada com sucesso!'); 
        }
    } else if (tipoIngresso == 'pista') {
        let restantePista = (quantidadePista.textContent) - quantidade;
        if (restantePista < 0) {
            alert('Quantidade indisponível para pista!');
        } else{
            quantidadePista.innerHTML = (`${restantePista}`); 
            alert('Compra realizada com sucesso!'); 
        }
    }
}
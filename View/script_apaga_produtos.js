document.getElementById('delete-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const codProduto = form.cod_produto.value;

    fetch(`http://localhost:5000/produtos/${codProduto}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<p>${data.mensagem || data.erro || 'Produto excluído com sucesso.'}</p>`;
    })
    .catch(error => {
        document.getElementById('results').innerHTML = `<p>Erro: ${error.message}</p>`;
    });
});
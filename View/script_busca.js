document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const params = new URLSearchParams(formData);

    fetch(`http://localhost:5000/produtos?${params}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';

            if (data.message) {
                resultsDiv.innerHTML = `<p>${data.message}</p>`;
            } else if (Array.isArray(data)) {
                if (data.length === 0){
                    resultsDiv.innerHTML = `<p>Nenhum produto encontrado com os parâmetros informados.</p>`;
                } else {
                    let table = '<table><tr><th>Código</th><th>Nome</th><th>Categoria</th><th>Preço</th></tr>';
                    data.forEach(produto => {
                        table += `<tr><td>${produto.cod_produto}</td><td>${produto.nome_produto}</td><td>${produto.categoria}</td><td>${produto.preco_unitario}</td></tr>`;
                    });
                    table += '</table>';
                    resultsDiv.innerHTML = table;
                }
            } else if (data.cod_produto) {
                let table = '<table><tr><th>Código</th><th>Nome</th><th>Categoria</th><th>Preço</th></tr>';
                table += `<tr><td>${data.cod_produto}</td><td>${data.nome_produto}</td><td>${data.categoria}</td><td>${data.preco_unitario}</td></tr>`;
                table += '</table>';
                resultsDiv.innerHTML = table;
            } else {
                resultsDiv.innerHTML = `<p>Resposta da API em formato inesperado.</p>`;
            }
        })
        .catch(error => {
            document.getElementById('results').innerHTML = `<p>Erro: ${error.message}</p>`;
        });
});
# MOVIE MANAGER🎥

<b>📝Conceito do app</b>
<p>O aplicativo busca atuar de maneira similar ao Letterboxd, servindo como uma plataforma que permite que seja feita a busca de filmes por título, mostrando informações relevantes e possibilitando que seja feita a avaliação do filme com uma nota e comentário. Após a avaliação ser feita, ela fica guardada no banco de dados, podendo ser consultada, alterada ou excluída.</p>
<br>

 
<b>📝Setup do ambiente virtual</b>
<ul>
    <li>Liberar uso do ambiente virtual: python -m venv venv</li>
    <li>Ativar ambiente virtual: .\venv\Scripts\activate</li>
    <li>Instalar Django: pip install django</li>
    <li>Instalar Django Rest: pip install djangorestframework</li>
    <li>Instalar Requests: pip install requests</li>
</ul>
<br>


<b>📝Documentações relevantes</b>
<ul>
    <li>https://docs.djangoproject.com/en/5.0/</li>
    <li>https://www.django-rest-framework.org/</li>
</ul>
<br>


<b>📝API utilizada</b>
<ul>
    OMDb: The Open Movie Database
    <li>https://www.omdbapi.com/</li>
</ul>
<br>


<b>📝Testes no Insomnia</b>
<ul>
    Arquivo: Testes_Insomnia.json
    <li>Teste do list(): Retorna todos os filmes que já foram avaliados, que estão no banco de dados.</li>
    <br>
    <li>Teste do retrieve(): Retorna um filme baseado na busca pelo parâmetro 'nome' e valor [nome_do_filme]</li>
    <br>
    <li>Teste do create(): Função que cria possibilita a avaliação de um filme. Para fazer o teste, preencher os espaços brancos nos campos 'nome' com o título do filme desejado, 'nota' com a nota dada e 'comentario' com a avaliação escrita no json. Campos disponibilizados no body>json: {"nome": " ", "nota": " ", "comentario": " "}. Após a avaliação, a tela exibirá uma mensagem de "Avaliação enviada", e ela poderá ser vista voltando ao teste do list(). Avaliações devem ser feitas para que possam ser armazenadas no banco de dados e as outras funções possam ser testadas.</li>
    <br>
    <li>Teste do update(): Função que possibilita que seja alterada a nota e comentários previamente dados para um filme. Para fazer o teste, buscar o filme que se deseja alterar a avaliação utilizando a numeração do filme no banco de dados e colocando o número na url (exemplo: http://127.0.0.1:8000/review/25/ >>> para alterar o filme 25), após isso, preencher os espaços brancos nos campos 'nota atualizada' com a nota nova para o filme desejado e 'comentario atualizado' com a avaliação nova no json. Campos disponibilizados no body>json: {"nota atualizada": " ", "comentario atualizado": " "}. Após a alteração, a tela exibirá uma mensagem de "Avaliação atualizada", e ela poderá ser vista voltando ao teste do list().</li>
    <br>
    <li>Teste do destroy(): Função que possibilita que seja excluído um filme do banco de dados. Para fazer o teste, buscar o filme através da numeração dele pela url (exemplo: http://127.0.0.1:8000/review/25/ >>> para excluir o filme 25). Após isso, a tela exibirá uma mensagem de "Avaliação excluída", e o filme não aparecerá mais no teste do list().</li>
    <br>
</ul>
<br>
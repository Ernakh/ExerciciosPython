import requests

urlposts = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(urlposts)
    response.raise_for_status() # Lança uma exceção para códigos de status de erro (4xx ou 5xx)

    data = response.json() # Converte a resposta JSON em um dicionário Python
    print("Resposta GET:")
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    
    
    
url = "https://randomuser.me/api/"
parametros = {"userId": 1}

try:
    response = requests.get(url, params=parametros)
    response.raise_for_status()

    usuarios = response.json()
    print("\nUsuários:")
    print(usuarios)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    

urlpost = "https://jsonplaceholder.typicode.com/posts"
novo_post = {
    "title": "Meu Novo Post",
    "body": "Este é o conteúdo do meu novo post.",
    "userId": 1
}

try:
    response = requests.post(urlpost, json=novo_post)
    response.raise_for_status()

    novo_item = response.json()
    print("\nResposta POST:")
    print(novo_item)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    
    
urlp = "https://jsonplaceholder.typicode.com/posts"
parametros = {"userId": 1}

try:
    response = requests.get(urlp, params=parametros)
    response.raise_for_status()

    posts_do_usuario = response.json()
    print("\nPosts do Usuário 1:")
    print(posts_do_usuario)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    
    
urlc = "https://httpbin.org/headers"
cabecalhos = {"User-Agent": "Meu Script Python"}

try:
    response = requests.get(urlc, headers=cabecalhos)
    response.raise_for_status()

    print("\nResposta com Cabeçalhos Personalizados:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
    
    
    
urlr = "https://randomuser.me/api/"
parametros = {"results": 10}

try:
    response = requests.get(urlr, params=parametros)
    response.raise_for_status()

    usuarios = response.json()
    print("\nUsuários:")
    print(usuarios)

except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")

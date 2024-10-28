# scraping-mercadolivre

Sobre o projeto:

1. Varredura
 > src > coleta > Spiders > mercadolivre.py
- Scrapy faz uma varredura nas 10 primeiras páginas do site informado e coleta as informações especificadas no código.

2. Coleta
  > data > data.jsonl 
- No bash executamos o comando abaixo para iniciar spider mercadolivre e especificamos que a saída dos dados coletados pelos spider
devem ser salvos em um arquivo data em formato jsonl.
    ```bash
    scrapy crawl mercadolivre -o data.jsonl 
    ```

3.Transformação
 > src > transformacao > main.py
- Usando pandas transformamos e tratamos os dados para ficarem mais legiveis.
- Criamos um banco de dados SQLite 
- Salvamos os dados tratados nesse banco 
    ```bash
    python
    ```


Para rodar projeto execute os passos abaixo após abrir projeto em uma IDE:

Criar ambiente virtual no projeto 
```bash
python -m venv .venv 
```

Entre no ambiente virtual
```bash
source .venv/Scripts/activate
```

Instale o streamlit
```bash
pip install streamlit
```

Entre na pasta src
```bash 
streamlit run dashboard/app.py 
```


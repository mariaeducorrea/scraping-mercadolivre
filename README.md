# scraping-mercadolivre

Sobre o projeto:

1. Coleta 
- Diretório:  src > coleta > Spiders > mercadolivre.py
- Scrapy faz uma varredura nas 10 primeiras páginas do site informado e coleta as informações especificadas no código.
- No bash foi executado o comando abaixo para iniciar spider mercadolivre e especifiquei que a saída dos dados coletados pelos spider
devem ser salvos em um arquivo data em formato jsonl.
->Executar bash dentro do diretório src:
```bash
scrapy crawl mercadolivre -o data.jsonl 
```

3. Transformação
- Diretório: src > transformacao > main.py
- Usando pandas transformei e tratei os dados para ficarem mais legiveis, criei/conectei um banco de dados SQLite e salvei os dados tratados nesse banco.
->Executar bash dentro do diretório src:
```bash
python transformacao/main.py
```

4. Dashboard
- Diretório: src > dashboard > app.py
- Usei o streamlit para jogar os dados do banco em um dashboard.
->Executar bash dentro do diretório src:
```bash 
streamlit run dashboard/app.py 
```

_________________________________________________________________________________________________________

Executar projeto:

Abrir projeto em IDE.

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


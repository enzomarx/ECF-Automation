# ECF Automation

Este projeto automatiza a transmissão do ECF para várias empresas utilizando o Domínio Web Thomson Reuters e o app ECF da Receita Federal. A automação é realizada utilizando `pyautogui` para simular interações com a interface do usuário e `tkinter` para criar uma interface gráfica para o usuário. O `pandas` é utilizado para manipulação dos dados das empresas a partir de um arquivo CSV.
a
## Estrutura de Diretórios

ecf_automation/
│
├── src/
│ ├── init.py
│ ├── automation.py
│ └── gui.py
│
├── data/
│ └── empresas.csv
│
├── assets/
│ └── README.md
│
├── tests/
│ ├── init.py
│ └── test_automation.py
│
├── requirements.txt
└── README.md


- `src/`: Contém os arquivos fonte do projeto.
  - `__init__.py`: Torna este diretório um pacote Python.
  - `automation.py`: Contém o código para a automação da transmissão do ECF.
  - `gui.py`: Contém o código para a interface gráfica do usuário.
- `data/`: Contém os arquivos de dados, como o CSV com as empresas e códigos.
  - `empresas.csv`: Arquivo CSV contendo as informações das empresas.
- `assets/`: Diretório para arquivos adicionais, como screenshots, documentação adicional, etc.
  - `README.md`: Explicação sobre o conteúdo dos assets.
- `tests/`: Contém testes automatizados para o projeto.
  - `__init__.py`: Torna este diretório um pacote Python.
  - `test_automation.py`: Arquivo de testes para o código de automação.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Documentação principal do projeto.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/ecf_automation.git
    cd ecf_automation
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

## Uso

1. Coloque o arquivo `empresas.csv` no diretório `data/` com as informações das empresas.
2. Execute a interface gráfica do usuário:
    ```bash
    python src/gui.py
    ```

3. Insira o período desejado e clique em "Iniciar" para iniciar a automação.

## Dependências

- `pyautogui`: Biblioteca para automação da interação com a interface do usuário.
- `tkinter`: Biblioteca para criação de interfaces gráficas.
- `pandas`: Biblioteca para manipulação de dados.
- `time`: Biblioteca padrão do Python para controle de tempo.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.



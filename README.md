# ECF Automation

Este projeto automatiza a transmissão do ECF para várias empresas utilizando o Domínio Web Thomson Reuters e o app ECF da Receita Federal. A automação é realizada utilizando `pyautogui` para simular interações com a interface do usuário e `tkinter` para criar uma interface gráfica para o usuário. O `pandas` é utilizado para manipulação dos dados das empresas a partir de um arquivo CSV. Além disso, o projeto utiliza Flask-SocketIO para atualizar logs em tempo real na interface web.

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

1. **Execute o servidor Flask-SocketIO:**
    ```bash
    python app.py
    ```

2. **Execute o script de automação:**
    ```bash
    python automatizacao.py
    ```

3. **Acesse a interface web para visualizar os logs em tempo real:**
    Abra um navegador web e vá para `http://127.0.0.1:5000/`.

## Dependências

- Python 3.x
- pyautogui
- pandas
- tkinter
- Flask
- Flask-SocketIO
- socketio

Certifique-se de que todas as dependências estão listadas no arquivo `requirements.txt`.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob direitos reservados ao autor.
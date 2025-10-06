# Torre de Hanói com Busca A*

Este projeto implementa o **algoritmo A*** para resolver o problema clássico da **Torre de Hanói**.
O código está escrito em **Python 3**.

---

## **Requisitos**

* Python 3.8 ou superior
* Qualquer editor de código (VS Code, PyCharm, Jupyter Notebook, etc.) ou terminal/Prompt de Comando
* Para Google Colab: navegador e conta Google

---

## **Instruções de Execução**

### **1. Windows 10/11**

1. Instale o [Python](https://www.python.org/downloads/) (se ainda não tiver) e marque a opção **"Add Python to PATH"** durante a instalação.
2. Salve o arquivo Python (`buscaAestrela.py`) em uma pasta de sua preferência.
3. Abra o **Prompt de Comando** (`cmd`) e navegue até a pasta do arquivo usando `cd`.

   ```cmd
   cd C:\caminho\para\o\arquivo
   ```
4. Execute o código com:

   ```cmd
   python buscaAestrela.py
   ```
5. O programa irá imprimir o **caminho da solução** passo a passo.

---

### **2. Linux (Ubuntu, Debian, Fedora, etc.)**

1. Abra o terminal.
2. Verifique se o Python 3 está instalado:

   ```bash
   python3 --version
   ```

   Caso não esteja, instale-o (Ubuntu/Debian):

   ```bash
   sudo apt update
   sudo apt install python3
   ```
3. Salve o arquivo Python (`buscaAestrela.py`) na pasta desejada.
4. Navegue até a pasta do arquivo:

   ```bash
   cd /caminho/para/o/arquivo
   ```
5. Execute o código:

   ```bash
   python3 buscaAestrela.py
   ```
6. O terminal exibirá cada estado da solução.

---

### **3. Google Colab**

1. Acesse [Google Colab](https://colab.research.google.com/).
2. Crie um novo notebook (`File -> New Notebook`).
3. Copie e cole todo o código Python da Torre de Hanói no notebook.
4. Execute a célula clicando no botão **Play** (ou `Shift + Enter`).
5. O output exibirá a **sequência de estados** até a solução final.

---

## **Observações**

* Para aumentar o número de discos, altere o parâmetro `n_discos` na chamada:

  ```python
  caminho = a_star_iniciar(6)
  ```
* Tenha em mente que **o tempo de execução cresce exponencialmente** com o número de discos devido à complexidade do problema.


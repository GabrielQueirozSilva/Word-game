**Introdução**

Este é um projeto antigo que criei para uma matéria. Ele consiste em um jogo no qual palavras são mostradas em uma área e você tem que digitar a tradução. O sistema mostra um quadrado verde se você acertou e um vermelho se errou. Você escolhe a palavra que aparece e a tradução dela; ele foi feito focado em praticar palavras pouco lembradas de uma língua até você memorizá-las.

Estou postando-o aqui principalmente por causa do arquivo sv.py, onde aprendi muito sobre SQL. Abra o arquivo para um entendimento melhor.

**Como Jogar**

Primeiramente, é preciso ter três itens principais:

* **Python 3.11**: Versão utilizada no desenvolvimento.
* **MySQL**: Necessário para o armazenamento e persistência dos dados.
* **Sistema Operacional**: Desenvolvido e testado em Windows.

Com tudo pronto, crie uma venv para o funcionamento do jogo na pasta raiz do projeto usando o comando:

```bash
python -m venv venv
```

Depois, ative o ambiente virtual:

```bash
venv\Scripts\Activate
```

Instale as dependências presentes no arquivo requirements.txt via pip. Nele constam os requisitos tanto do servidor quanto do cliente (necessário pois a matéria pedia um sistema cliente-servidor).

Com tudo pronto, rode primeiro o servidor em um terminal e, depois, abra outro terminal para rodar o apr.py.
Aqui está o seu texto corrigido, mantendo exatamente a mesma estrutura e os links originais, apenas ajustando a gramática, ortografia e pontuação:

Ao rodar o apr.py você se deparará com essa tela:
<img width="999" height="785" alt="Captura de tela 2026-03-26 212140" src="https://github.com/user-attachments/assets/27108178-679f-4176-8e2c-4b6e3a0e5df7" />

Esta é a tela inicial do jogo. Como o projeto foi planejado para ter mais funcionalidades, existe espaço para mais 3 botões. O jogo não possui um "X" ou seta de voltar; para retornar à tela anterior, aperte ESC. Caso volte para uma tela errada, aperte ESC novamente.

Clicando no botão "I know", você irá para a tela inicial do jogo de palavras:
<img width="999" height="789" alt="Captura de tela 2026-03-26 213236" src="https://github.com/user-attachments/assets/2150b2a5-8eec-469f-a827-0ceb8438e54f" />

Com essa tela aberta, você verá 4 botões. O botão "Add word" serve para adicionar uma palavra nova; você deve ir primeiramente nele, pois inicialmente os outros não funcionarão. Ao abri-lo, você será direcionado para a seguinte tela:
<img width="995" height="788" alt="Captura de tela 2026-03-26 212157" src="https://github.com/user-attachments/assets/27e0b5cd-e4b2-417c-96e4-f2e4653f9fca" />

Nesta tela, você adiciona primeiramente a palavra que aparecerá e depois a tradução dela. Escreva ambas neste formato: "Hello,olá" e aperte enter. Lembre-se de colocar a vírgula separando ambas, pois o comando a utiliza como distinção. Uma caixa de mensagem aparecerá indicando o resultado da operação, assim como uma mensagem no terminal. Feita a operação, aperte ESC e volte à tela inicial.

O botão "let's try" é o jogo em si; ao apertá-lo, você será direcionado a esta tela:
<img width="992" height="786" alt="Captura de tela 2026-03-26 212233" src="https://github.com/user-attachments/assets/acb1e58e-5c65-4c10-ab2f-3d20540f8147" />

Nesta tela aparecerá a palavra original, assim como um espaço embaixo para você escrever a tradução. Caso você acerte, o quadrado à direita da caixa de texto ficará verde; caso contrário, ficará vermelho, e no terminal aparecerá a tradução correta. As palavras têm pontos de acerto, portanto, a quantidade de acertos ou erros de uma certa palavra influencia a frequência com que ela aparecerá.

Nesta tela também existem mais 3 botões:

*O botão "Reset" redefine os pontos de todas as palavras para que voltem a aparecer aleatoriamente;
*O botão "Edit" modifica a palavra em questão;
*O botão "I know" define uma palavra como aprendida, o que faz com que ela não apareça mais nesta tela (caso exista somente 1 palavra, você aperte em "I know" e tente adivinhar a próxima, o programa fechará).

Voltando à tela inicial do jogo, o botão "Revise" abrirá a seguinte tela:
<img width="999" height="784" alt="Captura de tela 2026-03-26 214252" src="https://github.com/user-attachments/assets/1841e409-501b-4bdd-b357-ec523daedce2" />

Esta tela é onde estão as palavras as quais você definiu como "I know", servindo para você revisá-las. O botão "Reset" aqui possui a mesma função mencionada anteriormente.

Por fim, voltando à tela inicial novamente, o botão "Edit" serve para editar uma palavra. Ele funciona melhor sendo acessado pela tela "I know", pois, na época, eu o configurei para selecionar a palavra atual e mostrá-la com uma caixa de texto vazia embaixo:
<img width="996" height="785" alt="Captura de tela 2026-03-26 212246" src="https://github.com/user-attachments/assets/9a999508-c3f3-4c52-8394-210073e3eaa2" />

O que você verá será o ID, o nome 1 e o nome 2. Para editar, escreva embaixo o nome 1 desejado, o nome 2 desejado e o estado da palavra (onde 1 = aprendida, vai para o "Revise"; e 0 = não aprendida, não vai para o "Revise"). Note que esta parte do estado pode não funcionar corretamente, pois provavelmente interrompi o desenvolvimento nesta etapa.

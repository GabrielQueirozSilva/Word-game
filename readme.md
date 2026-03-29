**Introdução**
Este é um projeto antigo que criei para uma matéria. Ele consiste em um jogo o qual palavras em ingles são mostradas e você tem que adivinhar a tradução delas, mostrando um quadrado verde se você acertou e um quadrado vermelho se não acertou.

Estou postando ele aqui principalmente por causa do arquivo sv.py, onde eu aprendi muito sobre sql. Abra o arquivo para um entendimento melhor.

**Como Jogar**
Primeiramente e preciso ter 3 coisas principais:

O python 3.11, versão compativel com o jogo, 
O jogo foi feito em um sistema operacional windows, apesar de eu não ter o conhecimento se funciona ou não em linux;
Também é necessario o mysql instalado para o armazenamento dos dados;

Com o tudo pronto, crie uma venv para o funcionamento do jogo na pasta raiz do projeto usando o comando:
```bash
python -m venv venv
```
Depois ative o ambiente virtual usando:
```bash
venv\Scripts\Activate
```
Ao fazer esses passos instale os requerimentos presentes no arquivo requeriments.txt pelo pip install, nele existe os requerimentos tanto do servidor quanto do cliente (precisei fazer assim pois a matéria pedia um sistema de servidor e cliente);

Com tudo feito, rode primeiramente o servidor em um terminal, e dois crie outro e rode o apr.py;

Ao rodar o apr.py você se deparará com essa tela:
<img width="999" height="785" alt="Captura de tela 2026-03-26 212140" src="https://github.com/user-attachments/assets/27108178-679f-4176-8e2c-4b6e3a0e5df7" />

Esta é a tela inicial do jogo, como o jogo foi planejado para ter mais coisas, existe espaço para mais 3 botões, o jogo não possui um X ou seta de voltar, volte para a tela anterior apertando esc, caso volte para uma tela errada aperte esc novamente;

Clicando no botão "I know", você irá para a tela inicial do jogo de palavras:
<img width="999" height="789" alt="Captura de tela 2026-03-26 213236" src="https://github.com/user-attachments/assets/2150b2a5-8eec-469f-a827-0ceb8438e54f" />

Com essa tela aberta você verá 4 botões:
O botão "Add word" serve para adicionar uma palvra nova, você deve ir primeiramente nele, pois inicialmente os outros não 
funcionaram. Ao abrir ele você será direcionado para a seguinte tela:
<img width="995" height="788" alt="Captura de tela 2026-03-26 212157" src="https://github.com/user-attachments/assets/27e0b5cd-e4b2-417c-96e4-f2e4653f9fca" />

Nesta tela, voce adiciona primeramente a palavra que aparecerá e depois a tradução dela. Escreva ambas neste formato: "Hello,ola" e aperte enter. Lembre-se de por a virgula separando ambas, pois o comando usa ela para distinguir. Uma caixa de mensagem aparecerá indicando o resultado da operação, assim como uma mensagem no terminal. Feito a operação aperte esc e volte a tela inicial;

O botão "let's try" é o jogo em si, ao apertar ele você será direcionado a esta tela:
<img width="992" height="786" alt="Captura de tela 2026-03-26 212233" src="https://github.com/user-attachments/assets/acb1e58e-5c65-4c10-ab2f-3d20540f8147" />


Nesta tela aparecerá a palavra original, assim como um espaço embaixo para você escrever a tradução. Caso você acerte, o quadrado a direita da caixa de texto ficará verde, caso não, ficará vermelho, e no terminal aparecerá a tradução. As palavras tem pontos de acerto, então a quantidade de acertos ou erros de uma certa palavra influencia a quantidade de vezes que ela aprecerá.

Nesta tela também tem mais 3 botões:
O botão "Reset" reseta os pontos de todas as palvras, para voltarem a aparecer aleatoriamente;
o botão "Edit" modifica a palvra em questão;
O botão "I know" define uma palavra como aprendida, o que faz ela não aparecer mais nesta tela (caso exista somente 1 palavra e voce aperta em i know, e tentar adivinhar a palvra, o progama fechará);

Voltando a tela inicial do jogo, o botão "Revise" abrirá a seguinte tela:
<img width="999" height="784" alt="Captura de tela 2026-03-26 214252" src="https://github.com/user-attachments/assets/1841e409-501b-4bdd-b357-ec523daedce2" />

Esta tela é onde estão as palavras as quais você definio como "I know" e aqui serve para você revisar elas, com tambe o botão reset fazendo a mesma função de antes;

Por fim, voltando a tela inicial novamente, o botão "Edit" serve para editar uma palavra, ele funciona melhor sendo usado pela tela "i know" pois na época eu fiz ele pegar a palavra direto que você está e mostrar ela com uma caixa de texto vazia embaixo:
<img width="996" height="785" alt="Captura de tela 2026-03-26 212246" src="https://github.com/user-attachments/assets/9a999508-c3f3-4c52-8394-210073e3eaa2" />

O que você ver será o id, o nome 1 e o nome 2, para editar, esceve embaixo o nome1 que voce deseja, o nome2 que você deseja e o estado dela que você deseja, 1= aprendida, vai pro revise, 0= não aprendida, não vai pro revise, mas esta parte não funciona, provavelmente parei o desenolvimento aqui

# 🎃 Pumpkindash (Demo Acadêmica)

Este repositório contém a **versão demonstrativa** do jogo *Pumpkindash*, um projeto desenvolvido exclusivamente como Trabalho Acadêmico para a faculdade utilizando a biblioteca **Pygame** em **Python** e compilado para um executável nativo do Windows.

> ⚠️ **Nota importante:** Este projeto foi concluído para fins de avaliação acadêmica. Não há planos para futuras atualizações, suporte ou continuidade do desenvolvimento.

Inspirado na precisão rítmica de *Geometry Dash* e ambientado em uma atmosfera sombria de *Halloween*, o jogo desafia o jogador a desviar de obstáculos macabros e testar seus reflexos para alcançar a maior pontuação.

---

## 🛠️ O que eu implementei nesta Demo

O foco principal do desenvolvimento foi aplicar boas práticas de programação, arquitetura limpa e **otimização de performance** (garantindo que o jogo rode liso e sem travamentos):

* **Arquitetura Orientada a Objetos:** Separação estruturada entre o jogador, constantes de configuração e o comportamento dinâmico dos obstáculos (`Obstacle`).
* **Otimização contra Engasgos (Anti-Stuttering):** Separação estrita entre o carregamento inicial de arquivos pesados (sprites e imagens) e o ciclo de reposicionamento das entidades. O uso de métodos `reset()` eliminou travamentos de CPU durante o gameplay.
* **Avaliação de Curto-Circuito (Short-Circuit):** Lógica de colisões e pontuação estruturada estrategicamente para poupar processamento da CPU frame a frame.
* **Gerenciamento de Caixa de Colisão:** Sincronização em tempo real entre as coordenadas físicas do jogo e o sistema de `Rect` do Pygame para garantir colisões precisas.

---

## 🚀 Como Baixar e Jogar (Sem necessidade de instalar o Python)

A demo foi compilada em um arquivo executável (`.exe`). Isso significa que **você não precisa ter o Python ou o Pygame instalados** no seu computador para jogar.

### 1. Baixar o Jogo
* Acesse o link do projeto no [Google Drive](INSERIR_LINK_DO_SEU_DRIVE_AQUI).
* Faça o download do arquivo compactado `Pumpkindash.zip`.

### 2. Extrair os Arquivos
* Clique com o botão direito no arquivo baixado e selecione **"Extrair Aqui"** (usando WinRAR, 7-Zip ou o próprio Windows).
* *Nota: É obrigatório extrair os arquivos. O jogo não funcionará se for executado diretamente de dentro do arquivo .zip.*

### 3. Executar o Jogo
* Abra a pasta que você extraiu e dê dois cliques no arquivo **`main.exe`**. O jogo abrirá imediatamente!

---

## 📂 Conteúdo do Arquivo

* `assets/`: Diretório contendo todas as texturas, sprites e imagens temáticas de Halloween necessárias para o funcionamento do jogo.
* `data/`: Diretório contendo um único arquivo em formato .txt, servindo para guardar as pontuações de jogadoras(e).
* `main.exe`: O executável do jogo compilado. Contém todo o código e dependências do projeto empacotados de forma nativa.

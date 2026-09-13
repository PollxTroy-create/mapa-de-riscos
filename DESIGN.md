# Design

## O mundo: Laudo Laboratorial

O laudo clínico já é o objeto que compara **o que você mediu** com **o que era esperado** — que é exatamente o que este jogo faz com a marcação do aluno. O jogo inteiro é um laudo sendo produzido: o aluno é o analista, os 15 setores são determinações, e a atividade termina com o laudo liberado e protocolado.

Escolhido pelo professor contra o sorteio (Caderno de Bancada) e contra o desafiante mais forte (Manual de Abas em Acetato). Risco assumido e declarado: é a direção mais previsível para esta categoria, então a execução precisa carregar o peso.

### Por que este mundo resolve o produto

| Problema do produto | O que o laudo já tem |
|---|---|
| Comparar marcação do aluno × referência | A coluna do valor obtido contra o intervalo de referência |
| Comunicar erro sem usar verde/vermelho | O **flag** de valor alterado: marca marginal, negrito e desvio tabular |
| Dar pressão competitiva sem infantilizar | **Corrida em controle** — sequência de determinações sem violação, vocabulário real de controle de qualidade (Westgard) |
| Navegar 15 unidades | A coluna de analitos: um eixo vertical único governando a página |
| Fechar a atividade com um comprovante | A **liberação do laudo** e seu número de protocolo |
| Tela de celular | Um laudo impresso *já é* uma coluna estreita |

## Cor

O laudo não tem cor decorativa. **Todo o croma da interface pertence ao código da NR-5** — nenhuma exceção, em nenhum estado.

```
--paper      #FBFAF6   papel do laudo (claro)
--paper-2    #F2EFE7   faixa de intervalo de referência
--ink        #14161A   impressão
--ink-2      #55525C   texto secundário
--ink-3      #8B8792   rótulos e unidades
--rule       #D9D4C7   fio de tabela
--rule-2     #B4AE9E   fio estrutural
--flag       #14161A   marca de alterado — forma, nunca cor
```

Escuro (mesma estrutura, papel invertido para leitura noturna no celular):

```
--paper      #121316   --paper-2 #1B1C21   --ink #ECEAE4
--ink-2      #A8A49C   --ink-3   #78747C   --rule #2C2D33   --rule-2 #43444C
```

**As cinco cores da NR-5 são idênticas nos dois temas** — são norma, não estilo. O anel preto e o rótulo do grupo garantem contraste.

```
físico #0E9F5B · químico #E03127 · biológico #7A4E2D · ergonômico #F2C200 · acidentes #1163A8
```

**Regra inviolável:** verde e vermelho nunca significam certo e errado. Acerto, omissão e excesso se comunicam por marca marginal, peso tipográfico e hachura. Toda célula de cor carrega também o nome ou a sigla do grupo — o conteúdo é codificado por cor e daltonismo é risco real aqui.

## Tipografia

Três famílias, cada uma com uma voz que significa algo:

| Papel | Família | Uso |
|---|---|---|
| Voz estrutural do documento | **Schibsted Grotesk** 400/500/700/900 | Títulos, rótulos de campo, cifras-herói (tabular) |
| Voz da máquina | **Spline Sans Mono** 400/600 | Valores, unidades, códigos, protocolo, contadores |
| Voz humana | **Newsreader** 400/500, itálico | Prosa de interpretação — o comentário do gabarito |

A separação é semântica: o que a máquina mediu é monoespaçado; o que uma pessoa interpreta é serifado. Medida de leitura 62–70ch. Escala por contraste, não por degraus intermediários.

## Composição

**O laudo é uma coluna.** No celular ele ocupa a largura toda; no desktop fica em medida fixa de ~780px, com a figura da planta ancorada ao lado. Nunca vira dashboard.

**Localizador recortado (a decisão de mobile):** em vez de espremer a planta 16:9 numa tela de 390px, cada determinação mostra **um recorte da planta na região daquele setor**, calculado a partir das coordenadas de bbox já mapeadas. A planta inteira fica a um toque de distância.

**Cinco posições fixas.** Os cinco grupos aparecem sempre como as mesmas cinco linhas, na mesma ordem, na mesma posição, nas 15 determinações e em todas as larguras. Na terceira rodada o polegar já sabe onde elas estão.

**O círculo é o controle.** Ele se monta em escala real enquanto o aluno marca, com leitura monoespaçada da proporção 1× / 2× / 4× — o aluno vê o que "grande" significa em vez de ler a palavra.

## Estados — vocabulário do laudo

`pendente` · `em determinação` · `liberado` · `alterado` (tem flag) · `conferido` (sem flag)

Confirmar chama-se **Liberar resultado** e é irreversível, como em bancada. O fechamento é **Liberar laudo**.

## Movimento

Um único momento autoral, usado duas vezes: **a impressão**. Ao liberar um resultado, os flags e a interpretação entram linha a linha, com avanço mecânico curto e ease-out exponencial, a partir de um estado já visível — as cinco linhas não são substituídas por outro painel, elas são **anotadas na margem onde já estavam**. Ao liberar o laudo, o protocolo carimba. Sob `prefers-reduced-motion` tudo assenta sem avanço.

## Proibido neste produto

- Verde ou vermelho como semântica de acerto/erro
- Confete, medalhas, mascote, barra de progresso arredondada
- Emoji ou glifo unicode como ícone — os ícones são SVG autorais de traço único
- Cor como único portador de significado
- Qualquer dominante de cor global sobre a interface

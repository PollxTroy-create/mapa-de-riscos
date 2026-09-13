# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

HTML/CSS/JS estático em arquivo único, sem build e sem framework. Publicado como Claude Artifact (`planta.jpg` viaja como arquivo de apoio). Restrição herdada da plataforma: CSP permite apenas scripts de cdnjs/jsdelivr/code.jquery e folhas de estilo apenas de fonts.googleapis.com; qualquer outro recurso externo é bloqueado silenciosamente. Sem backend. Downloads iniciados pela página não funcionam para o visitante.

## Users

Alunos de graduação em Biomedicina cursando Biossegurança (turma 2026), logo após a aula expositiva sobre mapas de risco. Jogam **durante a aula**, em 25–35 minutos, em uma mistura de celulares pessoais e notebooks — as duas classes de tela são igualmente importantes. Ambiente: sala de aula, possivelmente com o professor conduzindo em paralelo, conexão variável, alunos que podem parar e retomar.

Usuário secundário: o professor da disciplina, que precisa saber quem fez a atividade e que tipo de erro a turma cometeu, sem ter acesso a um backend.

## Product Purpose

Converter a atividade de fechamento da Aula 04 — "faça o mapa de riscos deste laboratório" — em um exercício com ciclo de feedback. O aluno percorre os 15 setores de um laboratório de análises clínicas, marca quais dos cinco grupos de risco da NR-5 estão presentes em cada um, gradua a intensidade, e recebe imediatamente o gabarito comentado daquele setor. Ao final, o mapa que ele desenhou aparece sobre a planta baixa, ao lado do mapa de referência.

Sucesso = o aluno sai sabendo (a) a qual grupo pertence cada agente, (b) que marcar risco a mais destrói o mapa tanto quanto marcar a menos, e (c) que o mapa não mostra tudo — a ausência de controles não vira círculo.

## Positioning

Não é um quiz de múltipla escolha sobre a NR-5. É uma vistoria: o aluno opera sobre a **planta baixa real** usada na aula, com os mesmos 15 setores numerados, e o artefato que ele produz é o próprio mapa de riscos — o entregável que a norma descreve. A pontuação é calibrada contra o erro característico da turma (marcar os cinco grupos em todo setor), não contra o acerto médio.

## Operating Context

- **A aula de origem:** 23 slides, terminando no estudo de caso do laboratório de análises clínicas (400 exames/dia, 13 trabalhadores, 15 setores numerados sobre uma planta baixa renderizada em 3D).
- **A norma:** NR-5. Cinco grupos de risco com cores normatizadas — Físico verde, Químico vermelho, Biológico marrom, Ergonômico amarelo, Acidentes azul. Diâmetro do círculo por intensidade: Pequeno 1×, Médio 2×, Grande 4×. Riscos simultâneos no mesmo ponto dividem o círculo em partes iguais.
- **Contexto legal atual:** a NR-05 atualizada não exige mais explicitamente o mapa de riscos, mas mantém obrigatórias a identificação e a comunicação dos riscos e determina que a CIPA registre a percepção de risco dos trabalhadores. O jogo precisa carregar essa nuance, não contorná-la.
- **Setor público:** em órgãos sob RJU, a responsabilidade é da CISTT, não da CIPA.
- Material de apoio do professor: `Aula 04 - Atividade Mapa de Riscos (redesenho + gabarito).md`, com o roteiro presencial em três momentos, o gabarito comentado dos 15 setores e a rubrica.

## Capabilities and Constraints

- **Fase 1 — Calibrar a legenda:** 12 pistas isoladas, cada uma pertencente a um grupo, com comentário imediato. Inclui as confusões características: perfurocortante (é Grupo 5, não 3), controle de produtividade (é Grupo 4), umidade (é Grupo 1), iluminação inadequada (é Grupo 5).
- **Fase 2 — Vistoria:** os 15 setores, um a um. Multi-seleção de grupos + graduação P/M/G por grupo. Ao confirmar, gabarito comentado do setor com quatro veredictos: essencial identificado, essencial omitido, defensável, não se sustenta. Contadores de acertos/omissões/excessos sempre visíveis. Navegação livre entre setores.
- **Fase 3 — Achados:** 5 riscos verdadeiros que não estão na lista numerada, misturados a 3 distratores.
- **Fim:** o mapa do aluno desenhado em SVG sobre a planta, alternável com o de referência e com a vista de diferenças; tabela setor a setor; diagnóstico do padrão de erro; código de conclusão.
- **Pontuação:** acerto +8, grau exato +3 (adjacente +1), omissão −5, excesso −10, risco defensável +2 (teto no máximo do setor). Máximo total 526. Calibrada e verificada: a estratégia "marcar tudo em todos os setores" rende 48%.
- **Persistência:** `localStorage` apenas. O aluno pode parar e retomar; nada sai do navegador dele.
- **Sem backend por decisão de produto:** declarar a capacidade `db` do Artifact tornaria a página restrita à organização e impediria os alunos de abrirem o link. O comprovante é o **código de conclusão** `MR-<pct>-<omissões><excessos>-<checksum>`, que o aluno envia ao professor e que não pode ser gerado sem jogar.

## Brand Commitments

- **As cinco cores da NR-5 são verdade normativa, não escolha de design.** Verde #0E9F5B físico, vermelho #E03127 químico, marrom #7A4E2D biológico, amarelo #F2C200 ergonômico, azul #1163A8 acidentes. Nenhuma direção visual pode alterá-las, reatribuí-las ou usá-las para outro significado.
- **Consequência direta:** verde e vermelho não podem significar "certo" e "errado" em lugar nenhum da interface — colidiriam com físico e químico. Acerto e erro se comunicam por forma, peso e tipografia.
- A escala 1×/2×/4× e a divisão do círculo em partes iguais são convenções da norma e precisam sobreviver a qualquer redesenho.
- A planta baixa (`planta.jpg`, 1006×565, com os 15 marcadores numerados em vermelho) é material da aula do professor e é a superfície sobre a qual o jogo acontece.

## Evidence on Hand

- `planta.jpg` — planta baixa do laboratório, extraída do slide 23 da aula. Coordenadas dos 15 marcadores e âncoras de desenho já mapeadas no código.
- Gabarito de 38 riscos essenciais + defensáveis + falsos positivos comentados, derivado do enunciado do caso e da NR-5.
- **Não existe e não deve ser fabricado:** dado real de dosimetria, medição de concentração, número de acidentes desta instituição, ou qualquer estatística de turma. O laboratório do caso é fictício.

## Product Principles

1. **O excesso custa mais que a omissão.** É o único jeito de ensinar que um mapa com círculo em todo cômodo deixou de informar — e informar é a única função que a NR-5 atribui a ele.
2. **Todo veredicto explica o porquê**, citando a pista do enunciado ou o item da norma. Feedback sem razão não corrige raciocínio.
3. **Ambiguidade honesta em vez de gabarito falso.** Riscos genuinamente discutíveis entram como "defensáveis": bonificam, nunca penalizam. Inventar certeza onde a norma não dá seria ensinar errado.
4. **A planta manda.** O aluno decide olhando o ambiente, não lendo alternativas. Pistas que só existem na planta — "Piso liso", a ausência de lava-olhos — valem tanto quanto as do texto.
5. **Setor 15 é o controle do experimento.** Um setor com um único risco médio existe para provar que nem todo cômodo é perigoso.

## Accessibility & Inclusion

- Sala de aula com telas de 390px a 1440px e iluminação variável; contraste e tamanho de alvo de toque são requisitos reais, não refinamento.
- Daltonismo é um risco concreto neste produto: o conteúdo é literalmente codificado por cor, e verde/vermelho/marrom são o eixo mais afetado. Cor nunca pode ser o único portador de significado — todo círculo e todo chip precisa carregar também nome, inicial ou número do grupo.
- `prefers-reduced-motion` precisa ser respeitado em qualquer camada de movimento.

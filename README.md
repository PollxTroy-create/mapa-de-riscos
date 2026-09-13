# Mapa de Riscos — Caça-Riscos

Jogo web para a disciplina de **Biossegurança**, graduação em Biomedicina.
Vistoria de riscos ocupacionais em um laboratório de análises clínicas, segundo
a **NR-5**.

**Jogar:** https://pollxtroy-create.github.io/mapa-de-riscos/

---

## O que é

O aluno assume a CIPA de um laboratório de análises clínicas — 400 exames por
dia, 13 trabalhadores, 15 setores — e emite o mapa de riscos como se emite um
laudo: determinação por determinação, cada resultado comparado com a
referência, cada divergência sinalizada na margem.

| Etapa | O que treina |
|---|---|
| **Calibração** | 12 pistas isoladas, uma por vez: a qual dos cinco grupos da NR-5 pertence cada uma. Inclui as confusões características — perfurocortante é Grupo 5, não 3; controle de produtividade é Grupo 4; umidade é Grupo 1; iluminação inadequada é Grupo 5. |
| **Determinações** | Os 15 setores, um a um, sobre a planta baixa. O aluno marca os grupos presentes e gradua a intensidade de cada um. Ao liberar o resultado, recebe o gabarito comentado daquele setor. |
| **Observações** | Cinco achados que não estão na lista numerada de setores, misturados a três distratores. |
| **Liberação** | O mapa que o aluno desenhou, sobre a planta, ao lado do de referência. Diagnóstico do padrão de erro e protocolo de conclusão. |

Tempo de jogo: **25 a 35 minutos**.

## A decisão pedagógica central

**Marcar risco a mais custa mais caro do que deixar de marcar** — excedente
−10, ausência −5. É o único jeito de ensinar que um mapa com círculo em todo
cômodo deixou de informar, e informar é a única função que a norma atribui a
ele.

A pontuação foi calibrada contra o erro característico da turma: a estratégia
"marcar os cinco grupos em todos os setores" rende **48%**, reprovada e com a
explicação por escrito.

Riscos genuinamente discutíveis entram como **defensáveis**: bonificam, nunca
penalizam. Inventar certeza onde a norma não dá seria ensinar errado.

## Cores

As cinco cores são normatizadas pela NR-5 e não são escolha de design:

| Grupo | Cor | |
|---|---|---|
| 1 · Físico | Verde | `#0E9F5B` |
| 2 · Químico | Vermelho | `#E03127` |
| 3 · Biológico | Marrom | `#7A4E2D` |
| 4 · Ergonômico | Amarelo | `#F2C200` |
| 5 · Acidentes | Azul | `#1163A8` |

Consequência que atravessa toda a interface: **verde e vermelho nunca
significam "certo" e "errado"**, porque colidiriam com risco físico e químico.
Acerto, ausência e excedente se comunicam por marca marginal, peso tipográfico
e hachura — e todo disco carrega também a inicial do grupo, para não depender
de cor.

## Protocolo de conclusão

Ao final o jogo emite um código `MR-<aproveitamento>-<ausências><excedentes>-<verificador>`
que o aluno envia ao professor. Registra o desempenho e o padrão de erro, e não
pode ser gerado sem jogar.

**Não há servidor.** O progresso fica no `localStorage` do navegador do aluno —
ele pode parar e retomar, e nada sai do dispositivo dele. Como o gabarito vive
no JavaScript da página, um aluno que abrir o código-fonte vê as respostas;
isso é inerente a um jogo estático e o protocolo não pretende ser à prova de
fraude.

## Arquivos

| | |
|---|---|
| `index.html` | O jogo inteiro. Autossuficiente: a planta baixa viaja embutida, não há dependência externa nem build. Abre por duplo clique, por e-mail ou em qualquer servidor estático. |
| `planta.jpg` | A planta baixa original, mantida como fonte. O jogo não a carrega — já está dentro do HTML. |
| `serve.py` | Servidor local de pré-visualização. Só existe porque o `http.server` padrão não declara charset e os acentos quebram. |
| `PRODUCT.md` · `DESIGN.md` | Registro das decisões de produto e do mundo visual. |

## Rodar localmente

```bash
python serve.py
```

Ou simplesmente abrir `index.html` no navegador.

---

Material didático. O laboratório do caso é fictício; os riscos, as pistas e o
gabarito derivam da NR-5 e da prática de análises clínicas.

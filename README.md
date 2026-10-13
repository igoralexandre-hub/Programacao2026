# -- BAIXAR O PROGRAMA PARA A MÁQUINA --

**Realizando o download dos arquivos do repositório para a máquina**

`git clone https://github.com/igoralexandre-hub/Programacao2026.git`

Baixa os arquivos do repositório do GitHub para o computador, criando uma pasta chamada `Programacao2026`.

**Atualizando os arquivos**

1. `cd Programacao2026`

   Entra na pasta do projeto.

2. `git remote update`

   Atualiza as informações dos repositórios remotos, verificando se existem novas alterações no GitHub.

3. `git pull`

   Baixa as alterações do GitHub e atualiza os arquivos do projeto no computador.

---

# -- ENVIAR O PROGRAMA PARA O REPOSITÓRIO --

**Configurando usuário e e-mail (identificação do autor das alterações)**

1. `git config user.name "usuario"`

   Define o nome que aparecerá como autor dos commits.

2. `git config user.email "email"`

   Define o e-mail que aparecerá como autor dos commits.

**Configurando o Git**

1. `git add *`

   Adiciona os arquivos modificados à área de preparação, deixando-os prontos para serem enviados em um commit.

2. `git commit -m "mensagem"`

   Salva as alterações em um commit no histórico do projeto. A mensagem deve descrever brevemente o que foi alterado.

3. `git push`

   Envia os commits para o repositório do GitHub, atualizando os arquivos disponíveis online.


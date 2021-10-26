# Evolução( Uma breve introdução)

# Introdução sobre redes neurais

&emsp;&emsp;Ultimamente no meu tempo livre estudo sobre IA, uma área bem interessante que para mim IA era parecido com uma “mágica", mas logo descobri que essa "mágica" por trás era matemática. Um tempo atrás fiquei sabendo sobre Aprendizado de máquina que tinha como base redes neurais humanas, o que para mim, parecia fantástico, e após pesquisar bastante, queria aplicar em algum projeto pessoal, foi quando nesse semestre durante a matéria de projeto de algoritmos tive a oportunidade, já que os projetos são bem livres. Ok até aí tudo bem, mas como posso conciliar aprendizado de máquina com estruturas de dados? E a resposta estava na minha frente, redes neurais e grafos. De grosso modo os neurônios de uma rede neural se comportam como um grafo, o corpo do neurônio sendo um nó e a aresta sendo o axônio do neurônio.

<center>

![](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/master/imgs/1-partes-do-neuronio.jpg)
</center>

<center>

[Imagem Neuronio](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/master/imgs/1-partes-do-neuronio.jpg)

</center>


<center>

![](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/master/imgs/rede-neural.png)

</center>

<center>

[Rede Neurais IA](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/master/imgs/rede-neural.png)

</center>

# Neuroevolução

&emsp;&emsp;Depois de alguns meses de pesquisa acabei achando um termo bem interessante, neuroevolução, daí para frente foi uma jornada bem desafiadora, porque usava muitos conceitos de biologia que não conhecia muito bem (não me dava muito bem com biologia no ensino médio). O modo de aprendizado natural de uma rede neural é uma estrutura fixa, ok até é tranquilo, agora vamos dar um dose dopaminérgica nos entusiastas de IA, o que você acha de evoluir essa rede neural usando algoritmos de evolução genética? Parece bem doido né haha,  logo abaixo iremos falar sobre isso, é eu sei isso é incrível!!!


&emsp;&emsp;Depois de alguns meses de pesquisa acabei achando um termo bem interessante, neuroevolução, daí para frente foi uma jornada bem desafiadora, porque usava muitos conceitos de biologia que não conhecia muito bem (não me dava muito bem com biologia no ensino médio). O modo de aprendizado natural de uma rede neural é uma estrutura fixa, ok até é tranquilo, agora vamos dar um dose dopaminérgica nos entusiastas de IA, o que você acha de evoluir essa rede neural usando algoritmos de evolução genética? Parece bem doido né haha,  logo abaixo iremos falar sobre isso, é eu sei isso é incrível!!!

&emsp;&emsp;É bem provável que você esteja se perguntando como podemos aplicar isso? Parece bem complicado não? E realmente sim, é complicado mesmo hahaha, mas para isso que existe python e suas bibliotecas, a principal biblioteca do python que faz esse algoritmo é a neat-python, mas o que é esse neat? O conceito de NEAT(NeuroEvolution of Augmenting Topologies) já é bem conhecido pela literatura, foi desenvolvido por Ken Stanley em 2002 na  Universidade do Texas em Austin é basicamente é um algoritmo genético para gerar redes neurais artificiais em evolução.

## Codificação 

&emsp;&emsp;Como foi dito anteriormente a base para essa solução e a biologia, logo herdamos alguns conceitos para essa solução, assim como na biologia temos o genótipo e fenótipo no NEAT também existe. Na codificação fazemos a representação dos indivíduos geneticamente em algoritmos, assim podemos reutilizar alguns conceitos do processo evolutivo como: seleção, mutação e cruzamento.

&emsp;&emsp;No caso o NEAT usa codificação direta. Uma codificação direta consiste em especificar explicitamente todos os detalhes sobre o indivíduo, ao respeitar ele como uma rede neural podemos perceber que cada gene está diretamente ligado ao um nó, assim ligando vários nós por conexões ponderadas, no final sempre tendo uma conexão direta e indireta entre o genótipo e fenótipo.

<center>

![](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/gh-pages/images/0_Kze4g6cLA3maofxq.png)

</center>
<center>

[Exemplo de nó e gene](https://raw.githubusercontent.com/projeto-de-algoritmos/Final-Flappy-Baby-Yoda/gh-pages/images/0_Kze4g6cLA3maofxq.png)

</center>
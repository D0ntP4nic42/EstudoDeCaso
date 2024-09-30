# Estudo De Caso
O código presente neste repositório tem como objetivo realizar a solução proposta para o estudo de caso de vibração no livro de Métodos Numéricos para Engenharia.

## Primeira Parte
Primeira parte do código deve corresponder a primeira parte da solução onde o Livro leva em consideração o carro em uma pista lisa.

Aqui utilizamos essa equação:  

$$
x(t) = cos{(0.05\mu)} + \frac{\lambda}{\mu} \cdot sen{(0.05\mu)}
$$

Abrindo essa equação com as fórmulas:  

$$\mu = \frac{\sqrt{(|c^2 - 4mk|)}}{2m}$$

e

$$\lambda = \frac{c}{2m}$$

Temos:

$$
x(t) = cos{(0.05 \cdot \sqrt{\frac{k}{m} - \frac{c^2}{4m^2}})} + \frac{c}{\sqrt{4km - c^2}} \cdot sen{(0.05\sqrt{\frac{k}{m} - \frac{c^2}{4m^2}})}
$$

<<<<<<< HEAD
Como queremos que o primeiro momento de equilíbrio ocorra em t = 0.05
e sabemos que x = distância da posição de equilíbiro da mola (Deve ser zero em t = 0.05) podemos igualar a equação a zero e com as informações passadas no estudo de caso podemos procurar um $k$ que satisfaça essa equação.
=======
Como queremos que o primeiro momento de equilíbrio ocorra em t = 0.05 e sabemos que x = distância da posição de equilíbiro da mola (Deve ser zero em t = 0.05) podemos igualar a equação a zero e com as informações passadas no estudo de caso podemos procurar um $k$ que satisfaça essa equação.
>>>>>>> c2bde49a028bb892d599cad8182f9bf2b9594662

### Achando o $k$:
Para achar o $k$ optei por utilizar o método da bisseção assim como o livro. Optei por esse método no código por sua similaridade com o método de busca binária. Para começar o método da bisseção escolhemos $k_1$ e $k_2$ tais que se $k_1$ aplicado na equação resulta em um número positivo então $k_2$ deve resultar em um negativo.  
  
O livro propõe dois valores iniciais para $k_1$ e $k_2$, não consegui compreender de onde veio a proposição, imagino que através do rascunho de um gráfico da equação seria possível aproximar uma opcção de valor com um resultado maior e um menor que 0.  
  
Após a seleção dos dois valores podemos simplesmente fazer iterações e calcular o resultado usando $k = \frac{k_1 + k_2}{2}$ o código calcula o resultado para esse $k$ e substitui o $k_1$ ou $k_2$ de acordo com o resultado, dessa forma podemos aproximar um valor de $k$ que zere a equação.

## Segunda Parte
A segunda parte do código deve corresponder a segunda parte da solução onde o livro leva em consideração o carro em uma pista rugosa.

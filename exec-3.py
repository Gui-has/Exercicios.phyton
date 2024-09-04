#os pares de instruções abaixo produzem o mesmo resultado? imprima os valores abaixo,veja se algum deles (a,b ou c) possuem valores diferentes nas versões 1e2, e caso sim,expliquenum comentario o motivo

#versão1
a=(4/2)+(2/4)
print(a)

b=4/(2+2)/4
print(b)

c=(4+2)*2-4
print(c)

#versão2
a=4/2+2/4
print(a)

b=4/2+2/4
print(b)

c=4+2*2-4
print(c)

NOTA: OS RESULTADOS NÃO SÃO OS MESMOS

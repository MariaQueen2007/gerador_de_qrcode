lista_letras = ['z,y,u,v,w,x,t,s,r,q,p,o,n,m,l,k,i,j,h,g,f,e,d,c,b,a']

def bubble_short(lista):
    for n in range(len(lista) -1, 0, -1):
        for i in range(n):
            if lista[i] > lista [i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

bubble_short(lista_letras)
print(lista_letras)
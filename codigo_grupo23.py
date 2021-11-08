## Códigos Tarea 2 Matemáticas Discretas Grupo 23

# Pregunta 2:
# Implementación naive de la fórmula recursiva

#cantidad_piramides: int int -> int
def cantidad_piramides(S,B):
    """Calcula la cantidad de piramides posibles con S pilas y B bloques """
    piramides=0
    if S == 0 or B == 0 or B < S:
      return 0
    elif S == 1 or S == B:
      return 1
    for i in range(1,S+1):
      piramides += cantidad_piramides(i,B-S)*(S-i+1)
    return piramides

# Ejemplo

cantidad_piramides(100,169) # 235555651928

# Pregunta 3:
# Implementación más eficiente utilizando programación dinámica

import numpy as np
#C_eficientes: int int -> int
def C_eficiente(S,B):
    """Entrega la cantidad de piramides con S pilas y B bloques"""
    if S==0: #Caso sin pilas
      return 0
    else:
      F=np.zeros((B+1,S+1),dtype=int)
      np.fill_diagonal(F,1) #Casos donde S = B
      F[:,1]=1 #Casos donde S = 1
      F[0,0]=0 #Caso B = 0 y S = 0, aquí esto puede ser redundante,
      # pero sin esta línea había errores. No debería afectar la eficiencia.
      F[0,1]=0 #Caso B = 0 y S = 1
      for i in range(2,B+1):
        for j in range(2,S+1):
          if i>j:
            for k in range(1,j+1):
              F[i][j]+=F[i-j][k]*(j-k+1)
      return F[B][S]

# Ejemplo 

C_eficiente(100,169) #  235555651928


# Pregunta 4 y 5
# Implementación de algoritmo para generar pirámides

#piramides: list list -> list
def piramides(Mg,Mc):
  """Crea piramides a partir de otras piramides """
  n=len(Mg)
  m=len(Mc)
  Lista=[]
  for i in range(n-m+1):
    l=[]+Mg
    for j in range(m):
      l[i+j]=Mg[i+j]+Mc[j]
      L=l
    Lista.append(L)
  return Lista

#generar: int int -> list
def generar(S,B):
  """Se generan todas las piramides de S pilas y B bloques"""
  if S == B: #caso base piramide
    return [list(np.ones(S,dtype=int))]
  #Matriz donde calcularemos las piramides necesarias para el calculo
  M=np.zeros((B-S+1,B-S+1),dtype=object)
  M.fill([[0]])
  #Casos base con S=1
  for i in range(1,B-S+1):
    M[i][1]=[[i]]
  #Creamos las piramides necesarias
  for i in range(1,B-S+1):
    for j in range(2,i+1):
      if i==j:
        x=np.ones((1,j),dtype=int)
        M[i][j]=x.tolist()
      if i>j:
        L=[]
        y=np.ones(j,dtype=int)
        Mg=y.tolist()
        for a in range(1,j+1):
          c=C_eficiente(a,i-j)
          for b in range(c):
            Mc=M[i-j][a][b]
            p=piramides(Mg,Mc)
            L+=p
          M[i][j]=L
  #Calculamos lo que buscamos
  if B>S:
    L=[]
    y=np.ones(S,dtype=int)
    Mg=y.tolist()
    for a in range(1,S+1):
      c=C_eficiente(a,B-S)
      for b in range(c):
        Mc=M[B-S][a][b]
        p=piramides(Mg,Mc)
        L+=p
  return L


# Por último la función dibujar imprime todas las posibles pirámides

def dibujar(lista):
  pilas = len(lista[0])
  for i in range(len(lista)):
     lineas = []
      arreglo = lista[i]
      maximo= max(arreglo)
      for j in range(maximo):
        string = ""
        for k in range(pilas):
          if arreglo[k] != 0:
            string = string + "1 "
            arreglo[k] = arreglo[k] - 1
          else:
            string = string + "0 "
        lineas.append(string)
      for j in range(len(lineas)):
        print(lineas[maximo-j-1])
      print("")
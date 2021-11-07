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
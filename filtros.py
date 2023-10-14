from PIL import Image
import numpy as np

def aplicar_filtro (mat:list, filtro:list) -> list:
    '''
    La funcion recibe dos arrays, uno de la imagen y otro del filtro, 
    para posteriormente aplicar el array filtro al array imagen, mediante una convolución
    -------------------------------------------------------------
    Args: 
    mat: el array imagen ingresada
    filtro: el filtro que elegio el usuario
    
    Return:
    resultado: el array imagen tras pasar por una convolución con el filtro
    '''
    f_altura, f_ancho = filtro.shape
    margen_altura = f_altura // 2
    margen_ancho = f_ancho // 2
    
    if len(mat.shape) != 2:
        mat = np.pad(mat,((margen_ancho,margen_ancho),(margen_altura, margen_altura), (0,0)), 'edge')
        canales = mat.shape[2]
    else:
        canales = 1 
    
    altura, ancho = mat.shape[:2]

    resultado = np.zeros((altura, ancho, canales), dtype=np.int64)

    for c in range(canales):
        for i in range(margen_altura, altura - margen_altura):
            for j in range(margen_ancho, ancho - margen_ancho):
                if canales == 1:
                    submat = mat[i-margen_altura:i+margen_altura+1, j-margen_ancho:j+margen_ancho+1]
                    resultado[i, j, c] = np.sum(submat * filtro)
                else:
                    submat = mat[i-margen_altura:i+margen_altura+1, j-margen_ancho:j+margen_ancho+1, c]
                    resultado[i, j, c] = np.sum(submat * filtro)
    resultado = resultado[margen_ancho: -margen_ancho, margen_altura:-margen_altura, :]
    return resultado

def normalizar (resultado:list) -> list:
    '''
    Para normalizar una imagen se debe calcular el minimo y maximo de la imagen, para posteriormente aplicar la formula de normalizacion,
    con esto poder cambiar la intensidad de los píxeles
    ------------------------------------------------------------------
    Args:
    resultado: array de numeros sin normalizar
    Return:
    resultado_img: mismo array de numeros tras normalizar
    '''
    valor_minimo = np.min(resultado)
    valor_maximo = np.max(resultado)
    resultado_normalizado = ((resultado - valor_minimo) / (valor_maximo - valor_minimo)) * 255

    if len(resultado_normalizado.shape) == 3 and resultado_normalizado.shape[2] == 3:
        resultado_img = Image.fromarray(resultado_normalizado.astype(np.uint8), "RGB")
    else:
        resultado_img = Image.fromarray(resultado_normalizado[:, :, 0].astype(np.uint8), "L")

    return resultado_img
    
def umbralizado (mat:list) -> Image:
    '''La funcion recibe el array de la imagen y compara los valores del mismo con el valor del umbral
    y de acuerdo, a si son mayores o menores que éste, los lleva a 255 o 0, respectivamente
    ------------------------------------------------------------------
    Args:
    mat: array de la imagen ingresada por el usuario
    Return:
    imagen: imagen tras aplicar el umbral
    '''
    try:
        canal = mat.shape[2]
    except:
        try:
            umbral = int(input('Ingrese el valor del umbral: '))
        except:
            return 'El umbral debe ser un número entero'
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if mat[i][j] > umbral:
                    mat[i][j] = 255
                elif mat[i][j] < umbral:
                    mat[i][j] = 0
        imagen = Image.fromarray(mat)
        return imagen
    else:
        return umbralizado_color(mat) 

def umbralizado_color (mat:list) -> Image:
    '''La funcion recibe el array de la imagen y hace un slicing para separar entre RGB 
    compara los valores del array con los respectivos valores del umbral según el color
    y, de acuerdo a si son mayores o menores que éste, los lleva a 255 o 0, respectivamente
    ------------------------------------------------------------------
    mat: array de la imagen ingresada por el usuario
    Return:
    imagen: imagen tras aplicar el umbral
    '''
    try:
        umbral_r = int(input('Ingrese el valor del umbral rojo: '))
        umbral_v = int(input('Ingrese el valor del umbral verde: '))
        umbral_a = int(input('Ingrese el valor del umbral azul: '))
    except:
        return 'Los umbrales deben ser números enteros'
    else:
        rojo = mat[:,:,0]
        verde = mat[:,:,1]
        azul = mat[:,:,2]
        for i in range(0,len(rojo)):
            for j in range(0,len(rojo[i])):
                if rojo[i][j] > umbral_r:
                    rojo[i][j] = 255
                else:
                    rojo[i][j] = 0
        for i in range(0,len(verde)):
            for j in range(0,len(verde[i])):
                if verde[i][j] > umbral_v:
                    verde[i][j] = 255
                else:
                    verde[i][j] = 0
        for i in range(0,len(azul)):
            for j in range(0,len(azul[i])):
                if azul[i][j] > umbral_a:
                    azul[i][j] = 255
                else:
                    azul[i][j] = 0
        imagen = Image.fromarray(mat)
        return imagen


def identidad (mat:list) -> Image:
    filtro = np.array([[0,0,0],[0,1,0],[0,0,0]])
    return aplicar_filtro(mat,filtro)
def negativo (mat:list) -> Image:
    filtro = np.array([[0,0,0],[0,-1,0],[0,0,0]])
    return aplicar_filtro(mat,filtro)
def sobel_vertical (mat:list) -> Image:
    filtro = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    return aplicar_filtro(mat,filtro)
def sobel_horizontal (mat:list) -> Image:
    filtro = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    return aplicar_filtro(mat,filtro)
def sharpen (mat:list) -> Image:
    filtro = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    return aplicar_filtro(mat,filtro)
def gaussian (mat:list) -> Image:
    filtro = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])
    return aplicar_filtro(mat,filtro)
def unsharpen (mat:list) -> Image:
    filtro = np.array([[-1,-4,-6,-4,-1],[-4,-16,-24,-16,-4],[-6,-24,-36,-24,-6],[-4,-16,-24,-16,-4],[-1,-4,-6,-4,-1]])
    return aplicar_filtro(mat,filtro)
def box_blur (mat:list) -> Image:
    filtro = np.array([[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1]])
    return aplicar_filtro(mat,filtro)
def lens_blur (mat:list) -> Image:
    filtro = np.array([[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0]])
    return aplicar_filtro(mat,filtro)
def motion_blur (mat:list) -> Image:
    filtro = np.array([[0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0]])
    return aplicar_filtro(mat,filtro)
def personalizado (mat:list) -> Image:
    try:
        dim = int(input('Ingrese el tamaño del kernel: '))
    except:
        return 'El tamaño debe ser un número entero'
    else:
        if dim % 2 == 0:
            return 'El tamaño debe ser un número impar'
        else:
            try:
                kernel = []
                for i in range(dim):
                    row = []
                    for j in range(dim):
                        row.append(int(input('Ingrese el valor de la posicion ' + str(i) + ' ' + str(j) + ': ')))
                    kernel.append(row)
                print(kernel)
                kernel = np.array(kernel)
                return aplicar_filtro(mat,kernel)
            except:
                return 'El kernel debe ser una matriz de números enteros'
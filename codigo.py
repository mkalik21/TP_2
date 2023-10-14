import filtros as f
from PIL import Image
import numpy as np
def main ():
    try:
        img = input('Ingrese el nombre de la imagen: ')
        img = Image.open(img)
        mat = np.array(img)   
    except:
        print('La imagen no se encontró')
    else:    
        archivo = input('Ingrese el nombre del archivo a guradar: ').lower()
        if len(archivo) == 0:
            archivo = 'a'
        archivo = archivo.split('.')
        if archivo[-1] == 'png':
            '.'.join(archivo)
        else:
            archivo.append('png')
            archivo = '.'.join(archivo)
                    
        print("""    OPERACIONES
        -----------
        1. Umbralizar
        2. Identidad
        3. Negativo
        4. Sobel vertical
        5. Sobel horizontal
        6. Sharpen
        7. Gaussian
        8. Unsharpen
        9. Box blur
        10. Lens blur
        11. Motion blur
        12. Kernel personalizado
        """)
        filter = input("Escoja el filtro a aplicar: ")
        filter = filter.lower()
        if filter == 'umbralizado' or filter == 'umbralizar' or filter == '1':
            imagen_filtro = f.umbralizado(mat)
            if type(imagen_filtro) == str:
                print(imagen_filtro)
            else:
                imagen_filtro.show()
                imagen_filtro.save(archivo)
                print('Operación realizada con éxito!')
        elif filter == 'identidad' or filter == '2':
            id = f.identidad(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'negativo' or filter == '3':
            id = f.negativo(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'sobel vertical' or filter == '4':
            id = f.sobel_vertical(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'sobel horizontal' or filter == '5':
            id = f.sobel_horizontal(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'sharpen' or filter == '6':
            id = f.sharpen(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'gaussian' or filter == '7':
            id = f.gaussian(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'unsharpen' or filter == '8':
            id = f.unsharpen(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'box blur' or filter == '9':
            id = f.box_blur(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'lens blur' or filter == '10':
            id = f.lens_blur(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'motion blur' or filter == '11':
            id = f.motion_blur(mat)
            imagen_filtro = f.normalizar(id)
            imagen_filtro.show()
            imagen_filtro.save(archivo)
            print('Operación realizada con éxito!')
        elif filter == 'personalizado' or filter == 'kernel personalizado' or filter == '12':
            id = f.personalizado(mat)
            if type(id) == str:
                print(id)
            else:
                imagen_filtro = f.normalizar(id)
                imagen_filtro.show()
                imagen_filtro.save(archivo)
                print('Operación realizada con éxito!')
        else:
            print('El filtro no existe')

if __name__ == "__main__":
    main()
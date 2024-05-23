from PIL import Image
import os
files = os.listdir()
print(files)
files.remove('main.py')
if 'resized-images' in files:
    files.remove('resized-images')
else:
    os.mkdir('resized-images')
for NI in files:
    try:
        image = Image.open(NI)
        sunset_resized = image.resize((2200, 2200)) #RESOLUTION
        sunset_resized.save(fr'resized-images/{NI}')
        image.close
        print(f'{NI} foi RESIZED com sucesso!\n')
    
    except Exception as error:
        print(f'Não foi possivel fazer o RESIZE {error}')

input('O processo foi terminado\nENTER PARA FECHAR')

from PIL import Image
file_name = raw_input('jpg file: ')
file_name = 'image/' + file_name
im = Image.open(file_name)
pix = im.load()
txt_file_name = file_name[:-3] + 'txt'
with open(txt_file_name, 'w') as out:
    for i in range(224):
        for j in range(224):
            out.write(str(pix[i, j][0]) + '\n')
    for i in range(224):
        for j in range(224):
            out.write(str(pix[i, j][1]) + '\n')
    for i in range(224):
        for j in range(224):
            out.write(str(pix[i, j][2]) + '\n')

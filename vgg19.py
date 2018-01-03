import scipy.io
import fileinput
import glob
import numpy as np

with open('./vgg19_weight.txt', 'w') as out1, open('./vgg19_bias.txt', 'w') as out2:
    matpath = './imagenet-vgg-verydeep-19.mat'
    data = scipy.io.loadmat(matpath)
    vgg_layers = data['layers'][0]

    w = vgg_layers[0][0][0][0][0][0]
    b = vgg_layers[0][0][0][0][0][1]
    for i in range(64):
        for j in range(3):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[2][0][0][0][0][0]
    b = vgg_layers[2][0][0][0][0][1]
    for i in range(64):
        for j in range(64):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[5][0][0][0][0][0]
    b = vgg_layers[5][0][0][0][0][1]
    for i in range(128):
        for j in range(64):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[7][0][0][0][0][0]
    b = vgg_layers[7][0][0][0][0][1]
    for i in range(128):
        for j in range(128):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[10][0][0][0][0][0]
    b = vgg_layers[10][0][0][0][0][1]
    for i in range(256):
        for j in range(128):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[12][0][0][0][0][0]
    b = vgg_layers[12][0][0][0][0][1]
    for i in range(256):
        for j in range(256):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[14][0][0][0][0][0]
    b = vgg_layers[14][0][0][0][0][1]
    for i in range(256):
        for j in range(256):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[16][0][0][0][0][0]
    b = vgg_layers[16][0][0][0][0][1]
    for i in range(256):
        for j in range(256):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[19][0][0][0][0][0]
    b = vgg_layers[19][0][0][0][0][1]
    for i in range(512):
        for j in range(256):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[21][0][0][0][0][0]
    b = vgg_layers[21][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[23][0][0][0][0][0]
    b = vgg_layers[23][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[25][0][0][0][0][0]
    b = vgg_layers[25][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[28][0][0][0][0][0]
    b = vgg_layers[28][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[30][0][0][0][0][0]
    b = vgg_layers[30][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[32][0][0][0][0][0]
    b = vgg_layers[32][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[34][0][0][0][0][0]
    b = vgg_layers[34][0][0][0][0][1]
    for i in range(512):
        for j in range(512):
            for k in range (3):
                for l in range(3):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[37][0][0][0][0][0]
    b = vgg_layers[37][0][0][0][0][1]
    for i in range(4096):
        for j in range(512):
            for k in range (7):
                for l in range(7):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[39][0][0][0][0][0]
    b = vgg_layers[39][0][0][0][0][1]
    for i in range(4096):
        for j in range(4096):
            for k in range (1):
                for l in range(1):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

    w = vgg_layers[41][0][0][0][0][0]
    b = vgg_layers[41][0][0][0][0][1]
    for i in range(1000):
        for j in range(4096):
            for k in range (1):
                for l in range(1):
                    out1.write(str(w[k][l][j][i]) + ' ')
        out2.write(str(b[0][i]) + ' ')
    out1.write('\n')
    out2.write('\n')

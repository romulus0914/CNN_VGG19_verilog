import numpy as np
def softmax(w, t = 1.0):
    probs = np.exp(w - np.max(w))
    return probs / probs.sum(axis=0)
f = open('vgg19_output_1000.txt', 'r')
w = []
for line in f:
    w.append(float(line))
w_softmax = softmax(np.array(w))

with open('vgg19_predict.txt', 'w') as out, open('synset_words.txt', 'r') as classification:
    classes = classification.readlines()
    for j in range(5):
        max_prob = -1.0;
        for i in range(1000):
            if w_softmax[i] > max_prob:
                max_prob = w_softmax[i]
                max_label = i
        w_softmax[max_label] = 0
        out.write(str(max_label + 1) + ': ' + str(max_prob) + ' ' + classes[max_label])

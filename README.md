    Convolutional Neural Network of VGG19 model in verilog

    system architecture : cliffordwolf/picorv32
    CNN    architecture : VGG19 (imagenet-very-deep-vgg19.mat)

    some useful tools   : 
        vgg19.py           - analyize imagenet-very-deep-vgg19.mat(need to download by yourself) and output to vgg19_weight/bias.txt
                             # must generate by command "make vgg"
        image_converter.py - convert RGB value of .jpg(224*224) into .txt (in RGB order) by command "make image"
        softmax.py         - convert output of the model, vgg19_output.txt, into problilities of 1000 classes corresponding 
                             to synset_word.txt and write to vgg19_probs.txt by command "make softmax"

    image folder        : contains some .jpg files and its corresponding .txt and predict files

    execution           : "make pcpi"

    p.s it's not actually a trainable model, just a reconstruction of vgg19 to input an image and get its prediction.

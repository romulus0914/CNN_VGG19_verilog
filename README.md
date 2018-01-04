# CNN_VGG19_verilog

Convolutional Neural Network of VGG19 model in verilog

## system architecture

[cliffordwolf/picorv32](https://github.com/cliffordwolf/picorv32) - CPU with RISC-V ISA

## CNN architecture

VGG19 ([imagenet-very-deep-vgg19.mat](http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat)) - pretrained model by imagenet with 19 layers

## Some useful tools

tools written by myself that will help a lot 

### vgg19.py

analyize imagenet-very-deep-vgg19.mat(need to download by yourself) and output to vgg19_weight/bias.txt

```
make vgg
```

### image_converter.py

convert RGB value of .jpg(224 * 224) into .txt (in RGB order)

```
make image
```

### softmax.py

convert output of the model, vgg19_output.txt, into problilities of 1000 classes corresponding to synset_word.txt and write to vgg19_probs.txt

```
make softmax
```

## image folder        

contains some .jpg files and its corresponding .txt and predict files

## execution

```
    make pcpi
```

## p.s it's not actually a trainable model, just a reconstruction of vgg19 to input an image and get its prediction.

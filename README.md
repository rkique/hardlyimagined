# hardlyimagined
256x256 GAN and errata for the generation of artificial images. Used with Google Street View images to create exhibition. Model architecture based on Matthew Mann's GAN256. Modifications to outputs, save logic, filter count and kernel size (9x5 kernels for horizontal landscapes).

Images from various stages of training, collected into a studio piece:
![Example results](https://i.imgur.com/MXSJQc3.jpg)

There is also a fun tiling tool I have added. Here's an example Tiling.py result:

![Example results](https://i.imgur.com/NEecngs.jpg)
# How to use
I used Google Colab to host my project but any similar service should work. 
Make sure to have folders named Sprites, Results, and Models to save progress.
The image loading should take any images in the Sprites Folder; just make sure they are the right size (256x256) before running the GAN. Default save location for weights is in model 9999; the model will save and load from the same location automatically. Have fun!

On the sample I used, the model does not produce a wide range of results in latent space; however, by running the model with a single noise value as it evolves (as I do here), the variety is much better.



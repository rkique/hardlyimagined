# hardlyimagined
256x256 GAN and errata for artificial images. Used with Google Street View images to create exhibition. Based on Matthew Mann's GAN256, with modifications to outputs, save logic, filter count and kernels (9x5 kernels).

Images from various stages of training, collected into a studio piece:
![Example results](https://i.imgur.com/MXSJQc3.jpg)
Here's a gif going through model latent space (optimized for smaller viewing)
![Example results](https://media.giphy.com/media/TIFs0UqBgZkdCRzWrG/giphy.gif)

There is also a fun tiling tool I have added. Here's an example Tiling.py result:

![Example results](https://i.imgur.com/NEecngs.jpg)
# How to use
I used Google Colab to host my project but any similar service should work. 
Make sure you have folders named Sprites, Results, and Models to save progress.
The image loading should take any images in the Sprites Folder; just make sure they are the right size (256x256) before running the GAN. Default save location for weights is in model 9999; the model will save and load from the same location automatically. Have fun!

I found that this model (outdated architecture) does not produce a wide range of results in latent space; however, by running the model with a single noise value as it evolves (as I do here), the variety is much better.



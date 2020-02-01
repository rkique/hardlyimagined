# hardlyimagined
256x256 GAN and errata for artificial images. Used with Google Street View images to create exhibition. Based on Matthew Mann's GAN256, with modifications to outputs, save logic, filter count and kernels (9x5 kernels).


# How to use
I used Google Colab to host my project but any similar service should work. 
Make sure you have folders named Sprites, Results, and Models to save progress.
Change the image names to fit what it asks for, then run the GAN. Default save location for weights is in model 9999; the model will save and load from the same location automatically. Have fun!

I found that this model (outdated architecture) does not produce a wide range of results in latent space; however, by running the model with a single noise value as it evolves (as I do here), the variety is much better.


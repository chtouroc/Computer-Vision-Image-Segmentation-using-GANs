In order to reproduce our experiments, you need to use the code in 
https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix and to replace
the existing networks.py in "models" folder by our file networks.py, since 
it contains the changes that we made to consider Lovasz Hinge loss function. 

You need also to add lovasz_hinge.py in the "models" folder in order to use 
the Lovasz Hinge loss.

combine_A_and_B.py available in "datasets" folder needs to be replaced with our 
version in order to obtain a train and a test set with appropriate formats.

Concerning the test scores, we provide you with the metrics.py which allows 
the computation of the RMSE on test set provided by the code.
 
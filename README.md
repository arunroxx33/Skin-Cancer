Topic : Skin Cancer Detection using Malign or Benign

About

:
A tumor can be cancerous or benign. A cancerous tumor is malignant,
meaning it can grow and spread to other parts of the body. A benign tumor
means the tumor can grow but will not spread. Doctors diagnose skin
cancer in more than 3 million Americans each year, making it the most
common type of cancer.


Model Outline :

Step 1 : Image Preprocessing

● Read image
● Resize image
● Remove noise(Denoise)
● Segmentation
● Morphology(smoothing edges)


Step 2 : Use Basic model of Transfer Learning
Transfer learning is the idea of overcoming the isolated learning
paradigm and utilizing knowledge acquired for one task to solve
related ones.

Common Types of Transfer Learning Used :

● Inductive Transfer learning
● Unsupervised Transfer Learning
● Transductive Transfer Learning


Step 3 : Adding a CNN layer to refine the network and increase
It’s accuracy.

Dataset Sources :

● Skin Cancer MNIST: HAM10000
● Skin Cancer: Malignant vs. Benign

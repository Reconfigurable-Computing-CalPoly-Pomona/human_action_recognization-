#### Introduction
This repo contains both a tensorflow and pytorch approach for video human action recognition.  An InceptionV3 architecture is used to train the Tensorflow model, and 3D Convolutional Network architecture is used for PyTorch.

#### Building this project

This project contains source code for Tensorflow InceptionV3 and PyTorch 3D Convolutional Network algorithm. Here are steps in building this project.

1. Clone this repository.
2. Download the dataset from [UCF101](http://crcv.ucf.edu/data/UCF101/UCF101.rar) and extract.
3. Configure dataset in desired training method.
4. If running tensorflow, create folders train, test, sequences, and checkpoints in the data folder. Run 1_move_files.py and 2_extract_files.py to split dataset into train and test.  
5. If running PyTorch, run train.py to train the model. 

The original source code can be found at: 

PyTorch source: https://github.com/manoharvhr/PYNQ-Torch

PyTorch Training and Implementation: https://github.com/jfzhang95/pytorch-video-recognition

Tensorflow Training: https://github.com/harvitronix/five-video-classification-methods

Tensorflow Inference: https://github.com/dronefreak/human-action-classification


### Team Member:

Jonathan Hoong, Graduate student, Electrical and Computer Engineering department, College of Engineering, California State Polytechnic University, Pomona.

### Supervising Professor: 

**1. Mohamed El-Hadedy:** Assistant Professor, Electrical and Computer Engineering department, College of Engineering, California State Polytechnic University, Pomona.

**Collaborators:**

**1. Wen-Mei Hwu:**  Director of Center for Cognitive Computing Systems Research and Walter J. Sanders III-AMD Endowed Chair Professor in Elecrical and Computer Engineering at UIUC 

**2. Jinjun Xiong:** Director of Center for Cognitive Computing Systems Research and Adjunct Research Professor at UIUC  


### Project Structure:
PyTorch v1.2.0 has been successfully deployed on a PYNQ-Z1 board running on PYNQ OS v2.5. 

### Project Sponsors:

1. [Xilinx](https://www.xilinx.com/)

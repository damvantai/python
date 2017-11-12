# Some part of the code was referenced from below.
# https://github.com/pytorch/examples/tree/master/word_language_model 
import torch 
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
from data_utils import Dictionary, Corpus

# Hyper Parameters
embed_size = 128
hidden_size = 1024
num_layers = 1
num_epochs = 5
num_samples = 1000   # number of words to be sampled
batch_size = 20
seq_length = 30
learning_rate = 0.002

# Load Penn Treebank Dataset
train_path = './data/train.txt'
sample_path = './sample.txt'
corpus = Corpus()
ids = corpus.get_data(train_path, batch_size)
vocab_size = len(corpus.dictionary)
num_batches = ids.size(1) // seq_length
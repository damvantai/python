import torch
import os

class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0
        
    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1
   
    def __len__(self):
        return len(self.word2idx)
    
class Corpus(object):
    def __init__(self, path='./data'):
        self.dictionary = Dictionary()
        self.train = os.path.join(path, 'train.txt')
        self.test = os.path.join(path, 'test.txt')
        
    def get_data(self, path, batch_size = 20):
        # Add words to the dictionary
        with open(path, 'r') as f:
            tokens = 0
            for line in f:
                words = line.split() + ['<eos>']
                tokens += len(words)
                for word in words:
                    self.dictionary.add_word(word)
                    
        #
                  
                     
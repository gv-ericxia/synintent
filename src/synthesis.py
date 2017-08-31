#!/usr/bin/env python
# yibin.eric.xia@gmail.com

from __future__ import print_function

import nltk
from reader import Reader

class Synthesis(object):
  __input_tags = None
  __input_tagged_sents = None
  __output_tags = None
  __output_tagged_sents = None
  __output_text = None
  __verbose = False

  def __init__(self):
    # check nltk packages
    pass

  def verbose(self):
    self.__verbose = True

  def print_all(self):
    if self.__input_tags != None:
      print('input tags --------------------')
      for tag in self.__input_tags:
        print(tag)
    if self.__input_tagged_sents != None:
      print('input tagged sents ------------------')
      for sent in self.__input_tagged_sents:
        print(sent)
    if self.__output_tags != None:
      print('output tags ---------------------')
      for tag in self.__output_tags:
        print(tag)
    if self.__output_tagged_sents != None:
      print('output tagged sents ------------------')
      for sent in self.__output_tagged_sents:
        print(sent)
    if self.__output_text != None:
      print('output text -------------------=')
      print(self.__output_text)
      
  def optimize(self, tagged_sents):
    # optimize out some redundant parts
    self.__input_tagged_sents = tagged_sents
    self.__output_tagged_sents = tagged_sents
    for sent in self.__output_tagged_sents:
      print(sent)
      phrase_no = len(sent)
      print('%d phrases' %phrase_no)
      for phrase in sent:
        #new_phrase = phrase.__getitem__(0)
        #print(new_phrase)
        #print('phrase tag: ', phrase.label())
        self.remove_redundant(phrase)
    
  def remove_redundant(self, tree):
    # optimize out some redundant parts
    tree_no = len(tree)
    #print('%d branch' %tree_no)
    height = tree.height()
    tree_label = tree.label()
    #print('tree label: ', tree_label)
    if height == 2:
      #print('leaf:----')
      #print(tree)
      return
    index = 0
    remove_index = []
    for node in tree:
      index = index + 1
      #print(node)
      label = node.label()
      if label == 'ADJP' or label == 'PP-CLR' or label == 'PP':
        remove_index.append(index-1)
        pass
      elif label == ',' or label == '.':
        remove_index.append(index-1)
        pass
      else:
        self.remove_redundant(node)
    for i in reversed(remove_index):
      print('remove index: ', i)
      del tree[i]
    print('after deleting')
    print(tree)

if __name__ == '__main__':
  rdr = Reader()
  #rdr.verbose()
  tagged_sents = rdr.read_wsj_from_treebank(1)
  syn = Synthesis()
  syn.verbose()
  syn.optimize(tagged_sents)
  syn.print_all()
  

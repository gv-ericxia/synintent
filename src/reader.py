#!/usr/bin/env python
# yibin.eric.xia@gmail.com

from __future__ import print_function

import os
import nltk


class Reader(object):
  __input_text = None
  __sents = None
  __words = None
  __tags = None
  __nltk = False
  __verbose = False

  def __init__(self):
    # need to check installation of nltk packages
    self.__nltk = True
    pass

  def __reset(self):
    self.__input_text = None
    self.__sents = None
    self.__tagged_sents = None
    self.__words = None
    self.__tags = None
    
  def __print_all(self):
    if self.__sents != None:
      print('Sents:-------')
      for sent in self.__sents:
        print(sent)
    if self.__tagged_sents != None:
      print('Tagged sents:-------')
      for sent in self.__tagged_sents:
        print(sent)
    if self.__words != None:
      print('Words:-------')
      for word in self.__words:
        print(word)
    if self.__tags != None:
      print('Tags:--------')
      for tree in self.__tags:
        print(tree)

  def verbose(self):
    self.__verbose = True

  def get_tags(self):
    return self.__tags

  def get_tree(self, tree):
    return Tree(tree[0], [c if isinstance(c, basestring) else get_tree(c) for c in tree[1:]])

  def read_input(self):
    self.__reset()
    try:
      input = raw_input
    except NameError:
      pass
    self.__input_text = input()
    self.__sents = nltk.sent_tokenize(self.__input_text)
    '''
    from nltk.parse import stanford
    parser = stanford.GenericStanfordParser()
    self.__tagged_sents = parser.tagged_parse_sents(self.__input_text)
    '''
    self.__words = nltk.word_tokenize(self.__input_text)
    self.__tags = nltk.pos_tag(self.__words)
    if self.__verbose:
      self.__print_all()

  def read_textfile(self, filename):
    from nltk.corpus import PlaintextCorpusReader
    self.__reset()
    dirname = os.path.dirname(filename)
    basename = os.path.basename(filename)
    filelists = PlaintextCorpusReader(dirname, basename)
    real_filename = filelists.fileids()[0]
    self.__sents = filelists.sents(real_filename)
    self.__words = filelists.words(real_filename)
    self.__tags = nltk.pos_tag(self.__words)
    if self.__verbose:
      self.__print_all()
   
  def read_wsj_from_treebank(self, index):
    from nltk.corpus import treebank
    self.__reset()
    self.__input_text = 'wsj_000' + str(index) + '.mrg'
    self.__sents = treebank.sents(self.__input_text)
    self.__tagged_sents = treebank.parsed_sents(self.__input_text)
    if self.__verbose:
      self.__print_all()
    return self.__tagged_sents
    
  def check_syntax(self):
    # check typo, some punctuations, etc
    raise NotImplementedError()

if __name__ == '__main__':
  rdr = Reader()
  rdr.verbose()
  rdr.read_input()
  #rdr.read_wsj_from_treebank(1)
  #rdr.read_textfile('./test.txt')
  #rdr.check_syntax() 


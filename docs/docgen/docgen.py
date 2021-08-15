#!/usr/bin/python3

# -*- coding: utf-8 -*-
# --------------------------------------------------------------------
# Generates RST files from Simba sourcecode from the given root folder
# --------------------------------------------------------------------

import re
import os, sys

DOCNAME         = 'WaspLib'
IGNORE_FOLDERS  = ['.git', 'docgen']
FILE_EXTENSIONS = ['.simba'] 
SHORT_RST       = [('.. code-block:: pascal\n\n', '.. pascal::'), 
                   ('Example\n-------\n.. code-block:: pascal  ', 'Example\n-------')]

commentregex = re.compile('\(\*.+?\*\)', re.DOTALL)

def get_files(root): 
    ''' recursively walks every and graps every file name and path '''

    lst = os.listdir(root)
    result = []
    
    for name in lst:
      if os.path.isdir(root+os.sep+name):
        if not name in IGNORE_FOLDERS:
          result.extend(get_files(root+os.sep+name))
        continue

      _,ext = os.path.splitext(name)
      if ext.lower() in FILE_EXTENSIONS:
        result.append(root+os.sep+name)
    
    return result


def generate_index_rst(TOC):
    ''' 
      Generates the index.rst file 
      Builds a table of contents for every seperate folder
    '''
    index = 'Welcome to %s documentation!\n===============================\n\n' %  (DOCNAME,)
    
    for dir,value in TOC:
      # print('Linking: ' + dir)
      index += '.. toctree::\n   :maxdepth: 2\n\n	:caption: %s\n\n' % (dir.upper().replace(os.sep,' -> '),)
      
      for name in value:
        # print('   * ' + name)
        index += '   ' + name + '\n' 
      index += '\n-----------\n\n'

    i = open('source/index.rst', 'w+')
    i.write(index)
    i.close()
    
    
def generate(root):
    ''' 
      Generates RST by walking the specified directly
    '''
    
    if not os.path.exists('source'):
        os.mkdir('source')
    
    paths = get_files(root)
    NameToID = {}
    TOC = []
    
    added = set()
    
    for filename in paths:
      # print(filename)
    
      # extract path, directory name, and filename without extension
      path = os.path.dirname(filename)
      dir  = path[len(root)+1:]
      name = os.path.basename(os.path.splitext(filename)[0])
    
      # read in the sourcefile
      with open(filename, 'r') as f:
        contents = f.read()
      
      # if the file is already added to the set rename it so that
      # there will be no conflicts, expects the headers to have unique names
      if name in added: 
        name = name + '('+dir.replace(os.sep,'_')+')'
      added.add(name)
      
      
      # extract all comments
      res = commentregex.findall(contents)
      if len(res) == 0:
        print('WARNING: ', name, ' is not documented')
        continue
      
      # generate a output file
      out = open('source/%s.rst' % name, 'w+')
      
      # write the rst-style'd comments to the output file
      for doc in res:
        doc = doc[2:][:-2];
        for ptrn in SHORT_RST:
          doc = doc.replace(ptrn[1], ptrn[0])
        
        out.write(doc)
        out.write('\n\n')
        out.write('------------\n')
      out.close()
      
      # Table of Contents
      if dir.strip() == '': dir = 'root'
      if dir not in NameToID:
        NameToID[dir] = len(TOC)
        TOC.append((dir,[]))
      TOC[NameToID[dir]][1].append(name)

    # finally build the index file
    generate_index_rst(TOC)
    
    os.system('sphinx-build source build -c .')
	
if __name__ == '__main__':
    generate(sys.argv[1])
    
    if os.path.exists('source'):
        for filename in os.listdir('source'):
            os.remove('source' + os.sep + filename)
            
        os.rmdir('source') 

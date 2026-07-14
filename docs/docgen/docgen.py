#!/usr/bin/python3

# -*- coding: utf-8 -*-
# --------------------------------------------------------------------
# Generates RST files from Simba sourcecode from the given root folder
# --------------------------------------------------------------------

import re
import os, sys

DOCNAME         = 'WaspLib'
IGNORE_FOLDERS  = ['.git', '.github', 'docgen']
FILE_EXTENSIONS = ['.simba']

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

    index = "Welcome to |:bee:| %s documentation" %  (DOCNAME,)
    index += "\n"+ ("="*len(index)) + "\n\n" 
  
    class rstFile:
      def __init__(self, r, t):
        self.Root = r
        self.Text = t
        
    fileArr = []
    index += ".. toctree::\n    :titlesonly:\n"

    for dir,value in TOC:  

      print('Value: ' + str(value))
      fileName = os.path.splitext(dir)[0].split(os.sep)[0]
      if fileName == "root":
        continue

      fileRST = "source/" + fileName + ".rst"

      hasElement = False
      for f in fileArr:
        if f.Root == fileRST:
          hasElement = True
          break

      fileText = ""

      if not hasElement:
        fileArr.append(rstFile(fileRST, ""))
        if fileName != "root":
          index += "\n    " + fileName
      else:
        fileText += "\n\n-----------\n\n"
         
      if fileName != "root":   
        fileText += ".. toctree::\n  :maxdepth: 2\n  :caption: %s\n" % (dir.upper().replace(os.sep," -> "),)

      for name in value:
        fileText += "\n  " + name


      for f in fileArr:
        if f.Root == fileRST:
          f.Text += fileText
          break

    for f in fileArr:
      fileName = os.path.splitext(os.path.basename(f.Root))[-2]
      mdFile = "source" + os.sep + fileName + ".md"
      if os.path.exists(mdFile):
        tmp = open(mdFile, "a")
        tmp.write("\n" + "```{eval-rst}\n" + f.Text + "\n```")
      else:
        tmp = open(f.Root, "w+")
        title = os.path.splitext(os.path.basename(f.Root).upper())[0]
        title += "\n" + ("=" * len(title)) + "\n\n"
        tmp.write(title + f.Text)  
      tmp.close()


    i = open("source/index.rst", "w+")

    i.write(index)
    i.close()

def generate(root):
    ''' 
      Generates md by walking the specified directly
    '''   
    if not os.path.exists('source'):
      os.mkdir('source')
    
    paths = get_files(root)
    NameToID = {}
    TOC = []  
    added = set()
    
    for filename in paths:
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
        print("WARNING: ", name, " is not documented")
        continue
      
      # generate a output file
      out = open("source/%s.md" % name, "w+")
      # write the markdown-style'd comments to the output file
      for comment in res:  
        doc = comment[2:][:-2];
        out.write(doc)
        if comment != res[-1]:
          out.write('\n\n')
          out.write('- - -\n')
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
#!/usr/bin/env python
import os
import subprocess # just to call an arbitrary command e.g. 'ls'

class cd:
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

with cd("."):
   # we are in Dossier-Hg
   from subprocess import call, Popen, PIPE
   #call("ls")
   cmd = "pdflatex -interaction=batchmode _2016-05-LLN-Vortrag.tex"
   p = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   p.wait();
   cmd = "bibtex _2016-05-LLN-Vortrag"
   p = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   p.wait();
   cmd = "pdflatex -interaction=batchmode _2016-05-LLN-Vortrag.tex"
   p = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   p.wait();
   cmd = "pdflatex -interaction=batchmode _2016-05-LLN-Vortrag.tex"
   p = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   p.wait();

__author__ = 'wing2048'
import os
for file in os.listdir('.'):
    os.rename(file, file.replace(' ', '_'))
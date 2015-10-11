__author__ = 'wing2048'
import os

def underscore():
    for file in os.listdir('.'):
        os.rename(file, file.replace(' ', '_'))
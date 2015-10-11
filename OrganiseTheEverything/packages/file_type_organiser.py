__author__ = 'wing2048'
import os

ps = os.path.sep
ext_list = []


def organise():
    os.mkdir('by_extensions')
    for file in os.listdir('.'):
        if os.path.isdir(file):
            continue
        ext = os.path.splitext(file)[1].strip('.')
        if ext not in ext_list:
            ext_list.append(ext)
            try:
                os.mkdir('by_extensions' + ps + ext.strip('.'))
            except WindowsError:
                continue
        os.rename(file, 'by_extensions' + ps + ext + ps + file)
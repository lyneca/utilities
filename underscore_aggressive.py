import os


def underscore_bomb(dir):
    os.chdir(dir)
    for file in os.listdir('.'):
        print(file)
        if os.path.isdir(file):
            underscore_bomb(file)
        try:
            os.rename(file, file.replace(' ', '_'))
        except PermissionError:
            pass
    os.chdir('..')


underscore_bomb(os.getcwd())
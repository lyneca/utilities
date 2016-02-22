__author__ = 'wing2048'
from pydub import AudioSegment
import pydub.exceptions
import os
if not os.path.exists('./unconverted/'):
    os.mkdir('./unconverted/')
out_ext = input('Output file extension: ')
for file in os.listdir('.'):
    if os.path.isdir(file):
        continue
    print('[INFO] Target file: "%s"' % file)
    print('[FINE] Converting...')
    ext = file.split('.')[-1]
    name = '.'.join(file.split('.')[:-1])
    try:
        audio = AudioSegment.from_file(file, ext)
    except pydub.exceptions.CouldntDecodeError:
        print('[WARN] Couldn\'t convert.')
        continue
    audio.export(name + '.' + out_ext, out_ext)
    print('[FINE] Done.')
    print('[INFO] Moving original... ')
    os.rename(file, 'unconverted/'+file)
    print('[FINE] Done.')
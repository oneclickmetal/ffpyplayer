
__all__ = ('FFPyPlayer', 'set_log_callback', 'loglevels')


import os
import sys
from os.path import join
from os import environ
# needed for windows so dlls are found
ffmpeg_root = environ.get('FFMPEG_ROOT')
sdl_root = environ.get('SDL_ROOT')
if ffmpeg_root and os.path.exists(join(ffmpeg_root, 'bin')):
    bin_path = join(ffmpeg_root, 'bin')
    if bin_path not in os.pathsep.split(os.environ['PATH']):
        os.environ['PATH'] = bin_path + os.pathsep + os.environ['PATH']
if sdl_root and os.path.exists(join(sdl_root, 'bin')):
    bin_path = join(sdl_root, 'bin')
    if bin_path not in os.pathsep.split(os.environ['PATH']):
        os.environ['PATH'] = bin_path + os.pathsep + os.environ['PATH']
import ffpyplayer
from ffpyplayer import FFPyPlayer, set_log_callback, loglevels
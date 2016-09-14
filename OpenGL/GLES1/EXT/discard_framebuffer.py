'''OpenGL extension EXT.discard_framebuffer

This module customises the behaviour of the 
OpenGL.raw.GLES1.EXT.discard_framebuffer to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/discard_framebuffer.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.EXT.discard_framebuffer import *
from OpenGL.raw.GLES1.EXT.discard_framebuffer import _EXTENSION_NAME

def glInitDiscardFramebufferEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDiscardFramebufferEXT.attachments size not checked against numAttachments
glDiscardFramebufferEXT=wrapper.wrapper(glDiscardFramebufferEXT).setInputArraySize(
    'attachments', None
)
### END AUTOGENERATED SECTION
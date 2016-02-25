'''OpenGL extension ARB.clear_texture

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.clear_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	Texture objects are fundamental to the operation of OpenGL. They are
	used as a source for texture sampling and destination for rendering
	as well as being accessed in shaders for image load/store operations
	It is also possible to invalidate the contents of a texture. It is
	currently only possible to set texture image data to known values by
	uploading some or all of a image array from application memory or by
	attaching it to a framebuffer object and using the Clear or ClearBuffer
	commands.
	
	Both uploading initial texture data and clearing by attaching to a
	framebuffer have potential disadvantages when one simply wants to
	initialize texture data to a known value. Uploading initial data
	requires the application to allocate a (potentially large) chunk
	of memory and transferring that to the GL.  This can be a costly
	operation both in terms of memory bandwidth and power usage.
	Alternatively, attaching a texture level to a framebuffer to clear it
	may not be possible if the texture format isn't supported for
	rendering, or even if it is, attaching the image to a framebuffer object
	may cause the texture to be allocated in certain types of memory, which
	it may otherwise not need to be placed in.
	
	This extension solves these problems by providing a mechanism whereby
	the contents of a texture image array can be set to known values by
	using the ClearTexImage or ClearTexSubImage commands.  These commands
	can also be useful for initializing an image that will be used for
	atomic shader operations.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/clear_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.clear_texture import *
from OpenGL.raw.GL.ARB.clear_texture import _EXTENSION_NAME

def glInitClearTextureARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glClearTexImage.data size not checked against 'format,type'
glClearTexImage=wrapper.wrapper(glClearTexImage).setInputArraySize(
    'data', None
)
# INPUT glClearTexSubImage.data size not checked against 'format,type'
glClearTexSubImage=wrapper.wrapper(glClearTexSubImage).setInputArraySize(
    'data', None
)
### END AUTOGENERATED SECTION
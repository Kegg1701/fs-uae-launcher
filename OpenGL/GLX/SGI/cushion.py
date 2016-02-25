'''OpenGL extension SGI.cushion

This module customises the behaviour of the 
OpenGL.raw.GLX.SGI.cushion to provide a more 
Python-friendly API

Overview (from the spec)
	
	    This extension is directed at constant frame-rate applications.  Such
	    applications are written to ensure that a new image is generated every
	    N video frame periods, where N is itself a small constant integer.
	    If the application is unable to generate a frame within N video frame
	    periods, it is said to have dropped a frame.  Dropping a frame is a
	    *bad thing*.
	
	    Constant frame-rate applications make every effort to avoid dropping
	    frames.  In particular, they monitor the utilization of graphics
	    resources during the rendering of the current frame in order to predict
	    the behavior of subsequent frames.  If such prediction indicates that
	    a frame may be dropped, the rendering complexity of the frame is
	    reduced (e.g. by using models of lower geometric resolution) so as to
	    avoid the overload condition.
	
	    Unfortunately, because exact prediction is not possible, and because
	    there is no elasticity in the buffering of images, it is necessary
	    for constant frame-rate applications to under utilize the graphics
	    hardware.  This extension adds elasticity to the buffering of completed
	    images, in order to allow constant frame-rate applications to make full
	    use of the available graphics computation without dropping frames.
	    It further allows this elasticity to be controlled by the application in
	    order to minimize the introduction of latency that could otherwise
	    occur.
	
	    Applications that will benefit from this extension include simulation,
	    walk-through, and multimedia playback.
	
	    WARNING - Silicon Graphics has filed for patent protection for some
		      of the techniques described in this extension document.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGI/cushion.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.SGI.cushion import *
from OpenGL.raw.GLX.SGI.cushion import _EXTENSION_NAME

def glInitCushionSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
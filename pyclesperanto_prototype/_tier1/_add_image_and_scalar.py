from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def add_image_and_scalar(input : Image, output : Image = None, scalar : float = 1):
    """Adds a scalar value s to all pixels x of a given image X.
    
    <pre>f(x, s) = x + s</pre>
    
    Parameters
    ----------
    source : Image
        The input image where scalare should be added.
    destination : Image
        The output image where results are written into.
    scalar : float
        The constant number which will be added to all pixels.
        
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.add_image_and_scalar(, source, , destination, , scalar)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImageAndScalar    

    """


    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    }
    execute(__file__, 'add_image_and_scalar_' + str(len(output.shape)) + 'd_x.cl', 'add_image_and_scalar_' + str(len(output.shape)) + 'd', output.shape, parameters)

    return output

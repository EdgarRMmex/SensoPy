""""""

from distutils.core import setup
import sensopy

setup(name='sensopy',
      version=sensopy.__version__,
      description='TODO',
      author='Edgar Ramírez',
      author_email='typingmonkey9201@gmail.com',
      # py_modules=['sensopy'])
      packages=['sensopy', 'sensopy.discrim'])

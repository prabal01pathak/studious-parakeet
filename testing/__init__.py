"""
Description: init file for the package
"""

from .sum import sum, call_seconds
__version__ = '0.1.0'
__author__ = 'Prabal Pathak'
__email__ = 'prabal01pathak'
__status__ = 'Development'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2019 Prabal Pathak'
__all__ = ['__version__', '__author__', '__email__', '__status__', '__license__', '__copyright__']

def main():
    """
    Main function
    """
    print('Hello World!')
    sum(1, 2)
    call_seconds()
    return 0

if __name__ == '__main__':
    main()

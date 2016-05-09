#!/usr/bin/python
import sys
import os

def rename(file):
    """
    :type file: str
    """
    [fname, ext] = file.split('.')
    print 'fname is {}, and ext is {}'.format(fname, ext)
    [prefix, number] = fname.split('_')
    number = int(number)
    module = ''.join(['M', prefix[2:]])
    name = 'Wu'
    hw = ''
    if number <= 10:
        hw = 'blindcontour'
    elif number > 30:
        hw = 'sketchbook'
        number = number - 30
    else:
        hw = 'cheatalittle'
        number = number - 10
    ret = '_'.join([name, module, hw, str(number)])
    ret = '.'.join([ret, 'jpg'])
    os.rename(file, ret)
    return ret

def main(args):
    print sorted(map(rename, args))

if __name__ == '__main__':
    filenames = filter(lambda x: x[-4:] == '.jpg', os.listdir('./'))
    print filenames
    main(filenames)

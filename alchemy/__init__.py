'''
A functional, clean, responsive Pelican theme
'''


from pkg_resources import resource_filename


def path():
    '''
    Return path to theme templates and assets
    Use this as value for THEME in Pelican settings
    '''
    return resource_filename(__name__, '')

# -*- coding: UTF-8 -*-
#
#    X I E R P A   3
#    OS X Application (c) 2014 buro@petr.com, www.petr.com, www.xierpa.com
#    Authors: Petr van Blokland, Michiel Kauw–A–Tjoe
#
#    No distribution without permission.
#

class Constants(object):
    DB = ''
    DOMAIN = 'www.xierpa.com'
    PORT = 8001
    HOST = '%s:%s' % (DOMAIN, PORT)
    LOGIN = ''
    PASSWORD = ''
    PUBLICKEY = ''

    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 600
    WINDOW_MESSAGEHEIGHT = 100

    PARAM_EVENT = 'event'
    PARAM_UPLOAD_CONTENT = 'upload.content'
    PARAM_UPLOAD_FILENAME = 'upload.filename'
    PARAM_UPLOAD_HOST = 'upload.host'
    PARAM_UPLOAD_LOGIN = 'upload.login'
    PARAM_UPLOAD_PUBLICKEY = 'upload.publickey'
    EVENT_XIERPAUPLOAD = 'xierpaupload'
    PATH_INDEXAJAX = '/index/ajax'
    TARGETID_UPLOADRESULT = 'targetid_uploadresult'

    VALID_EXTENSIONS = ['png', 'jpg', 'jpeg', 'tiff', 'tif']
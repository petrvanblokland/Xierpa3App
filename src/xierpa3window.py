# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    xierpa server
#    Copyright (c) 2014+  buro@petr.com, www.petr.com, www.xierpa.com
#    
#    X I E R P A  3  A P P
#    Distribution by the MIT License.
#
# -----------------------------------------------------------------------------
#
#    xierpa3window.py
#
from xierpa3.components.component import Component 
import vanilla
from constants import C

class Xierpa3Window(object):
    u"""
    Implementation of a vanilla-based GUI for the Xierpa 3 environment.
    """

    def __init__(self):
        u"""
        Initialize the window and open it.
        """
        self.w = vanilla.Window((C.WINDOW_WIDTH, C.WINDOW_HEIGHT), "Xierpa 3",
                closable=True, minSize=(200, 200), maxSize=(1600, 1000))
        self.w.templates = self.getXierpa3Options()
        self.w.open()
        
        self.openServer()

    def getXierpa3Options(self):
        options = ["Xierpa 3 Server", "HTML + Sass", "Kirby Template", "WordPress Template"]
        return vanilla.RadioGroup((10, 10, -10, 80), options, callback=self.radioGroupCallback)

    def radioGroupCallback(self, sender):
        print "radio group edit!", sender.get()

    # Server
    
    def openServer(self):
        # http://www.cocoawithlove.com/2009/07/simple-extensible-http-server-in-cocoa.html
        """
        socket = CFSocketCreate(kCFAllocatorDefault, PF_INET, SOCK_STREAM,
            IPPROTO_TCP, 0, NULL, NULL);
        if (!socket)
        {
            [self errorWithName:@"Unable to create socket."];
            return;
        }
         
        int reuse = true;
        int fileDescriptor = CFSocketGetNative(socket);
        if (setsockopt(fileDescriptor, SOL_SOCKET, SO_REUSEADDR,
            (void *)&reuse, sizeof(int)) != 0)
        {
            [self errorWithName:@"Unable to set socket options."];
            return;
        }
         
        struct sockaddr_in address;
        memset(&address, 0, sizeof(address));
        address.sin_len = sizeof(address);
        address.sin_family = AF_INET;
        address.sin_addr.s_addr = htonl(INADDR_ANY);
        address.sin_port = htons(HTTP_SERVER_PORT);
        CFDataRef addressData =
            CFDataCreate(NULL, (const UInt8 *)&address, sizeof(address));
        [(id)addressData autorelease];
         
        if (CFSocketSetAddress(socket, addressData) != kCFSocketSuccess)
        {
            [self errorWithName:@"Unable to bind socket to address."];
            return;
        }
        """
        # Notification
        """
            listeningHandle = [[NSFileHandle alloc]
        initWithFileDescriptor:fileDescriptor
        closeOnDealloc:YES];
     
    [[NSNotificationCenter defaultCenter]
        addObserver:self
        selector:@selector(receiveIncomingConnectionNotification:)
        name:NSFileHandleConnectionAcceptedNotification
        object:nil];
    [listeningHandle acceptConnectionInBackgroundAndNotify];
        """
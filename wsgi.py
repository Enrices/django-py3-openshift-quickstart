#!/usr/bin/env python
import os
import imp
import sys

# To specify where Django can find the settings.py file, containing all settings information.
# the value 'a.b.c' will point out '<sys_path>/a/b/c.py'
# the original line in Django 1.6 was :
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")
# the ".setdefault" disappeared we don't know why
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Adding <here>/wsgi/openshift to the list of system paths
sys.path.append(os.path.join('wsgi', 'openshift'))

#
# Below for testing only
#
if __name__ == '__main__':
    ip   = 'localhost'
    port = 8051
    zapp = imp.load_source('application', 'wsgi/application')

    from wsgiref.simple_server import make_server
    httpd = make_server(ip, port, zapp.application)
    httpd.serve_forever()
# Add this to make it work locally :
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
~                                          

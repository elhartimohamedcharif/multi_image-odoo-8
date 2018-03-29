# -*- coding: utf-8 -*-
from openerp import http
from openerp.addons.web.controllers.main import Binary
openerpweb = http
import simplejson
import time
import openerp
import os
import StringIO
from openerp.http import request
from PIL import Image



class Binary_multi(Binary):
    @http.route('/med/upload_image_multi')
    def upload_image_multi(self, req, callback, ufile):
        # TODO: might be useful to have a configuration flag for max-length file uploads
        out = """<script language="javascript" type="text/javascript">
                    var win = window.top.window;
                    win.jQuery(win).trigger(%s, %s);
                </script>"""
        data = ufile.read()
        if data:
            current_dat_time = time.strftime("%d%m%y%H%M%S")
            file_name = current_dat_time + "_" + ufile.filename
            addons_path = openerpweb.addons_manifest['web']['addons_path'] + "/web/static/src/img/image_multi/"
            if not os.path.isdir(addons_path):
                os.mkdir(addons_path)
            addons_path += file_name
            buff = StringIO.StringIO()
            buff.write(data)
            buff.seek(0)
            img = Image.open(buff)
            xsize, ysize = img.size
            if xsize >1000 and ysize > 1000:
                enlarged_size = map(lambda x: x/4, img.size)
            else:
                enlarged_size = img.size
            img = img.resize(enlarged_size,Image.ANTIALIAS)
            img.save(addons_path, quality=25, optimize=True)
            file_name = "/web/static/src/img/image_multi/" + file_name
            print "******************************"
            print len(data) # initial size
            print os.stat(addons_path).st_size # compressed size
            print "******************************"
            args = [os.stat(addons_path).st_size, file_name, ufile.content_type, ufile.filename, time.strftime("%m/%d/%Y %H:%M:%S")]
        else:
            args = []
        return out % (simplejson.dumps(callback), simplejson.dumps(args))
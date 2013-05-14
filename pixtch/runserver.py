# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os
import sys
from flaskPixtch import Pixtch
import const

sys.path.insert(0, '.')
application = None
app = Pixtch(__name__)


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


if __name__ == '__main__':
    if 'SERVER_SOFTWARE' in os.environ:
        #todo run on bae
        # http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/faq
        from bae.core.wsgi import WSGIApplication

        application = WSGIApplication(app)
        app.config[const.ENV_BAE] = True
        print "This is BAE environ"
    else:
        print "This is local environ"

    import datetime

    t = datetime.datetime.now()
    print __name__, '>>init..ok', t
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)


# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os
import sys
from flaskPixtch import Pixtch
import const

sys.path.insert(0, '.')
application = None
app = Pixtch(__name__)

if __name__ == '__main__':
    #todo http://markitup.jaysalvat.com/home/
    # http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/faq
    import datetime

    t = datetime.datetime.now()
    app.setup()
    print __name__, '>>init..ok', t
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)


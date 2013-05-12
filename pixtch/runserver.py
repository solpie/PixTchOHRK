# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os
from pixtch import Pixtch
application = app = Pixtch(__name__)

@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")

if __name__ == '__main__':
    import datetime
    t = datetime.datetime.now()
    print __name__, '>>init..ok', t
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)


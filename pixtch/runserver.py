# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os
from flaskPixtch import create_app

from module import db

if __name__ == '__main__':
    #todo http://markitup.jaysalvat.com/home/
    #todo flask-sqlalchemy fix sae bug
    #todo permission admin
    #todo manager 脚本命令
    #todo unit test
    # http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/faq
    ######
    app = create_app()
    db.init_app(app)
    app.setup()
    db.create_all(app=app)
    ########
    import datetime

    t = datetime.datetime.now()
    print __name__, '>>init..ok', t, app.config.get('SQLALCHEMY_DATABASE_URI')
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)


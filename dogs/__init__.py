import pymysql
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.---出错修改提示
pymysql.version_info = (1, 4, 6, 'final', 0)     #指定mysqlclient驱动版本要求高于1.3.13或更高
pymysql.install_as_MySQLdb()           # 启用pymysql的驱动模式， 否则不能用于django

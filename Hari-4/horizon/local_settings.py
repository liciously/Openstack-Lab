# edit

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '172.16.4.115:11211',
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

OPENSTACK_HOST = "172.16.4.115"
OPENSTACK_KEYSTONE_URL = "http://172.16.4.115:5000/v3"

TIME_ZONE = "Asia/Jakarta"

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = 'Default'
OPENSTACK_KEYSTONE_DEFAULT_ROLE = 'admin'

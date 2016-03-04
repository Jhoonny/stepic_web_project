CONFIG = {
    'mode': 'django',
    'environment': {
     'PYTHONPATH': '/path/to/custom/python/packages',
     },
     'working_dir': '/home/box/web/',
     'user': 'www-data',
     'group': 'www-data',
     'args': (
        '--bind=0.0.0.0:8000',
        '--workers=4',
        '--timeout=30',
        '--log-file=/home/box/web/error_logs.log',
        'settings',
    ),
}

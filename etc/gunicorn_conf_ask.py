CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web/ask/',
  'python': '/usr/bin/python',
  'args': (
    '--bind=0.0.0.0:80',
    '--workers=16',
    '--timeout=60',
    '--log-file=/home/box/web/error2_logs.log',
    'ask.wsgi:application',
  ),
}

import subprocess

subprocess.run([
    'sqlplus',
    'system/meronyeyenekonjo24@192.168.1.3:1521/XE',
    'dump.sql'
])

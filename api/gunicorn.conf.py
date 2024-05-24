from os import getenv

bind = f"{getenv(key="HOST", default="127.0.0.1")}:{getenv(key="PORT", default=8000)}"
wsgi_app = "general.wsgi:application"
workers = getenv(key="WORKERS", default=1)
threads = getenv(key="THREADS", default=1)

import multiprocessing

bind = "0.0.0.0:8000"
workers = max(2, multiprocessing.cpu_count() * 2 + 1)
threads = 2
worker_class = "gthread"
timeout = 60
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"

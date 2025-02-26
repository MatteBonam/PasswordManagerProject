import threading
import time

class AutoLock:
    def __init__(self, app, timeout=300):
        self.app = app
        self.timeout = timeout
        self.timer = None
        self.last_activity = time.time()
    
    def reset_timer(self):
        self.last_activity = time.time()
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.timeout, self.lock)
        self.timer.start()
    
    def lock(self):
        if time.time() - self.last_activity >= self.timeout:
            self.app.show_login()
    
    def stop(self):
        if self.timer:
            self.timer.cancel()

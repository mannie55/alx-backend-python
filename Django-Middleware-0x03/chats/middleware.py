import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        # Now we set up the logger
        self.logger = logging.getLogger('request_logger')
        handler = logging.FileHandler('requests.log')
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        



    def __call__(self, request):
        response = self.get_response(request)
        
        user = request.user
        if user.username: 
            user = request.user.username
        else:
            user = "Anonymous"
        path = request.path
        log_message = f"{datetime.now()} - User: {user} - Path: {path}"
        self.logger.info(log_message)
        
    
        return response
import os

class Config:
    # General Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Default secret key for Flask sessions
    SESSION_COOKIE_NAME = 'your_session_cookie_name'
    UPLOAD_FOLDER = 'static/uploads'  # Folder where files will be uploaded
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image file extensions
    DEBUG = os.environ.get('DEBUG', True)  # Whether to enable debugging mode in Flask

    # MongoDB Configuration
    MONGO_URI = os.environ.get('MONGO_URI','your_MongodbString') # eg:mongodb+srv://username:password@cluster0.phsy7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
    
    # Cashfree API Credentials
    #client id and secret can be found after resgistering at cashfree
    CASHFREE_CLIENT_ID = os.environ.get('CASHFREE_CLIENT_ID', ' your client id')    #eg:TEST10441503142baf2bc588bc0aed4b30514401
    CASHFREE_CLIENT_SECRET = os.environ.get('CASHFREE_CLIENT_SECRET', ' your client secret')   #eg:cfsk_ma_test_6c339c4956bed590cbe5bdccbf82127a_6c39c6a4
    CASHFREE_ENVIRONMENT = os.environ.get('CASHFREE_ENVIRONMENT', 'sandbox')  # Set environment ('sandbox' or 'production')

    #
    
import os

class Config:
    # General Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Default secret key for Flask sessions
    SESSION_COOKIE_NAME = 'your_session_cookie_name'
    UPLOAD_FOLDER = 'static/uploads'  # Folder where files will be uploaded
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed image file extensions
    DEBUG = os.environ.get('DEBUG', True)  # Whether to enable debugging mode in Flask

    # MongoDB Configuration
    MONGO_URI = os.environ.get('MONGO_URI', 
        'mongodb://zubair:1234@cluster0-shard-00-00.phsy7.mongodb.net:27017,'
        'cluster0-shard-00-01.phsy7.mongodb.net:27017,'
        'cluster0-shard-00-02.phsy7.mongodb.net:27017/farm_fresh?ssl=true&replicaSet=atlas-numoic-shard-0&authSource=admin&retryWrites=true&w=majority'
    )
    
    # Cashfree API Credentials
    CASHFREE_CLIENT_ID = os.environ.get('CASHFREE_CLIENT_ID', 'TEST10441503142baf2bc588bc0aed4b30514401')
    CASHFREE_CLIENT_SECRET = os.environ.get('CASHFREE_CLIENT_SECRET', 'cfsk_ma_test_6c339c4956bed590cbe5bdccbf82127a_6c39c6a4')
    CASHFREE_ENVIRONMENT = os.environ.get('CASHFREE_ENVIRONMENT', 'sandbox')  # Set environment ('sandbox' or 'production')

    #
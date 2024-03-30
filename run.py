# from app import app

# if __name__ == '__main__':
#     app.run(debug=True)
from app import app
from flask_cors import CORS

# Enable CORS for all routes
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='192.168.100.12', debug=True)
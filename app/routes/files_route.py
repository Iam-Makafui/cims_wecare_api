from ftplib import FTP
from io import BytesIO
from flask import Blueprint, jsonify, request

files_blueprint = Blueprint('files', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# FTP server credentials
FTP_SERVER = 'cmsystemfiles.atwebpages.com'
FTP_USERNAME = '3680657_cmstestchurch'
FTP_PASSWORD = 'v,Te(10r88!DJhWr'
FTP_UPLOAD_DIRECTORY = '/cms/uploads/profile_images/'

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route to upload profile image
@files_blueprint.route('/file/profileimage', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # Connect to FTP server
        ftp = FTP(FTP_SERVER)
        ftp.login(user=FTP_USERNAME, passwd=FTP_PASSWORD)

        # Set the current directory on the FTP server
        ftp.cwd(FTP_UPLOAD_DIRECTORY)

        # Upload the file to the FTP server
        file_data = BytesIO()
        file.save(file_data)
        file_data.seek(0)
        ftp.storbinary('STOR ' + file.filename, file_data)

        # Close FTP connection
        ftp.quit()

        # Construct the file URL on the FTP server
        file_url = f'ftp://{FTP_USERNAME}@{FTP_SERVER}{FTP_UPLOAD_DIRECTORY}{file.filename}'

        return jsonify({'message': 'File uploaded successfully', 'file_url': file_url}), 200
    else:
        return jsonify({'message': 'File type not allowed'}), 400

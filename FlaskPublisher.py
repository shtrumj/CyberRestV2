from flask import Flask, render_template, make_response, send_file
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, template_folder='output')
auth = HTTPBasicAuth()

users = {
    "trot": generate_password_hash("Tr0t@dmin!")
}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
@app.route('/getDomaincsv')
@auth.login_required
def getDomaincsv():
    return send_file('output/domains.txt',
                     mimetype='text/csv',
                     attachment_filename='domains.txt',
                     as_attachment=False)
@app.route('/getIPcsv')
@auth.login_required
def getIPcsv():
    return send_file('output/ip.txt',
                     mimetype='text/csv',
                     attachment_filename='domains.txt',
                     as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='7171')


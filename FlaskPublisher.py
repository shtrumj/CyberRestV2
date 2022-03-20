from flask import Flask, render_template
app = Flask(__name__, template_folder='output')

@app.route('/fortigate')
def fortigate():
    return render_template("domains.csv")

if __name__ == "__main__":
    app.run(debug=True)


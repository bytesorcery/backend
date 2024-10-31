from flask import Flask, request
from databaseHandling import *

app = Flask(__name__)
database = "test.db"

@app.route("/api/submit-contact", methods=["POST"])
def contactHandoff():
    if request.method == "POST":
        DatabaseHandling(
            firstName   = request.form.get("firstName")
            lastName    = request.form.get("lastName")
            eMail       = request.form.get("eMail")
            phoneNumber = request.form.get("phoneNumber")
            message     = request.form.get("message")
        )
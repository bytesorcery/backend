import os
from flask import Blueprint, request
from backend.databaseHandling import *

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/submit-contact", methods=["POST"])
def contactHandoff():
    try:
        if request.method == "POST":
            DatabaseHandling(
                database    = os.getenv("FLASK_DATABASE"),
                firstName   = request.form.get("firstName"),
                lastName    = request.form.get("lastName"),
                eMail       = request.form.get("eMail"),
                phoneNumber = request.form.get("phoneNumber"),
                message     = request.form.get("message")
            )
    except Exception as e:
        print(f"An error occurred while processing the contact form: {e}")
        return "Server Error", 500
    return "Success", 200
from sqlite3 import connect


class DatabaseHandling:
    def __init__( self, database,
                  firstName, lastName,
                  emailAddress, message, **kwargs
    ):
        db = connect(database)
        cursor = db.cursor()

        message = message.encode("utf=8")

        try:
            if kwargs["phoneNumber"]:
                phoneNumber = kwargs["phoneNumber"]\
                        .strip(" ")\
                        .strip("-")
        except KeyError:
            phoneNumber = ""

        cursor.execute(
            """
            INSERT OR IGNORE INTO contacts(
                firstName, lastName, eMail,
                phoneNumber, personalMessage
            ) VALUES( ?, ?, ?, ?, ? )
            """,
            ( firstName,
              lastName,
              emailAddress,
              phoneNumber,
              message      )
        )

        db.commit()
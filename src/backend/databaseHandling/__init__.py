from sqlite3 import connect


class DatabaseHandling:
    def __init__( self, database,
                  firstName, lastName,
                  eMail, message, **kwargs
    ):
        
        db = connect(database)
        cursor = db.cursor()

        #Create database schema if it doesn't exist
        with open("src/backend/databaseHandling/schema.sql", "r") as f:
            db.executescript(f.read())

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
              eMail,
              phoneNumber,
              message      )
        )

        db.commit()
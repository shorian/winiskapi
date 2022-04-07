import os

from winiskapi import create_app, db
from winiskapi.models import User

app = create_app(os.getenv("FLASK_CONFIG") or "development")


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


if __name__ == "__main__":
    app.run()

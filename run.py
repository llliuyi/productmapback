# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app import create_app,db


app = create_app()



if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

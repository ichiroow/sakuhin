from flask import Flask
from routes import main, edit, complete, delete

app = Flask(__name__)

# Blueprint登録
app.register_blueprint(main.bp)
app.register_blueprint(edit.bp)
app.register_blueprint(complete.bp)
app.register_blueprint(delete.bp)

if __name__ == '__main__':
    app.run(debug=True)

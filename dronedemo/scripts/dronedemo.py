from dronedemo.main import app


def cli_entry():
    app.run(host='0.0.0.0', port=5000)

from website import create_app
from jinja2 import Template

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
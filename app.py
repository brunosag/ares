from website import create_app
import os

app = create_app()


@app.template_filter("is_integer")
def is_integer(a):
    return a.is_integer()


if __name__ == '__main__':
    app.run(debug='RENDER' not in os.environ)

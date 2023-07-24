

# from api import app, db\
from api import asgi_app, db


# adding the shell context processor
# @app.shell_context_processor
# def make_shell_context():
#     return {"app": app,
#             "db": db
#             }

# @asgi_app.shell_context_processor
# def make_shell_context():
#     return {
#         "app": asgi_app,
#         "db": db
#     }


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0",  load_dotenv=True)
    asgi_app.run(debug=True, host="0.0.0.0", load_dotenv=True, port=5000)
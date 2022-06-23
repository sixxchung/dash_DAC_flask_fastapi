from re import I
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from dashapp import create_dash_app
Path_for_dash = '/dash'
Port_for_dash = 8050

app_fastapi = FastAPI()
app_fastapi.router.redirect_slashes = False

app_dash = create_dash_app(requests_pathname_prefix=Path_for_dash)
app_fastapi.mount(Path_for_dash, WSGIMiddleware(app_dash.server))


@app_fastapi.get("/")
def redirect_root():
    #url = "http://0.0.0.0:" + str(port_dash) + urlPath_dash
    url = "http://0.0.0.0"+":"+str(Port_for_dash)+Path_for_dash+"/"
    # print(f"sixx==>{url}")
    response = RedirectResponse(url)
    return response

# @app_fastapi.get("/")
# def read_main():
#     return {
#         "routes": [
#             {"method": "GET", "path": "/", "summary": "Landing"},
#             {"method": "GET", "path": "/status", "summary": "App status"},
#             {"method": "GET", "path": "/dash",
#                 "summary": "Sub-mounted Dash application"},
#         ]
#     }

@app_fastapi.get("/status")
def get_status():
    return {"status": "ok"}

# A bit odd, but the only way I've been able to get prefixing of the Dash app
# to work is by allowing the Dash/Flask app to prefix itself, then mounting
# it to root
# dash_app = create_dash_app(requests_pathname_prefix="/dash")
# app_fastapi.mount("/dash", WSGIMiddleware(dash_app.server))

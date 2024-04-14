from fastapi import FastAPI, Request  
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()

origins = ['*']
test = "Rajesh"

# #  pasting CORAS CODE #################
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})



import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import openai
import markdown

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/submit-form')
async def submit_form(request: Request, user_content: str = Form(...)):
    openai.api_key = "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"
    results = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": ""},
        ]
    )
    content = results["choices"][0]["message"]["content"]
    content = markdown.markdown(content,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                ])
    return templates.TemplateResponse("result.html", {"request": request, "content": content})


if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=9000, reload=True)

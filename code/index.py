import uvicorn
from fastapi import FastAPI
import openai

app = FastAPI()


@app.get('/')
async def gpt(api_key, user_content: str, system_content: str = "", assistant_content: str = ""):
    """基于 fastapi 的 gpt-3.5-turbo 项目, 用于快速部署,方便API请求调试"""
    openai.api_key = api_key
    results = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ]
    )
    return results


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
app = FastAPI()


@app.get('/{fruta_verdura}')
async def main(fruta_verdura):
    return FileResponse(f"images/{fruta_verdura}.jpg")


#======= Linha para rodar no https://replit.com/====
#uvicorn.run(app,host="0.0.0.0",port="8080")


#=======comando para rodar a API localmente=========
#uvicorn app:app --reload
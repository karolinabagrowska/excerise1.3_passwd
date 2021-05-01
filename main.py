from fastapi import FastAPI
from fastapi import FastAPI, Response, status
from fastapi import FastAPI, HTTPException
import hashlib
app = FastAPI()


@app.get("/auth")
def password_get(response: Response, password = "", password_hash = ""):
    #password_hash = hashlib.sha512(("haslo").encode('utf-8'))
    #print(password_hash.hexdigest())
    #password_hash = hashlib.sha512(password.encode())


    password_sha512 = hashlib.sha512(password.encode('utf-8')).hexdigest()
    if password_sha512 == password_hash:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response.status_code
    else:
        raise HTTPException(status_code=401)
        
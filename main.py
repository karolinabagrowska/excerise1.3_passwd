from fastapi import FastAPI
from fastapi import FastAPI, Response, status
import hashlib
app = FastAPI()


@app.get("/auth", status_code = 200)
def password_get(password, password_hash, response: Response):
    #password_hash = hashlib.sha512(("haslo").encode('utf-8'))
    #print(password_hash.hexdigest())
    #password_hash = hashlib.sha512(password.encode())
    password_sha512 = hashlib.sha512(password.encode('utf-8')).hexdigest()
    if password_sha512 == password_hash:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response.status_code
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return response.status_code

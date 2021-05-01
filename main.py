from fastapi import FastAPI
from fastapi import FastAPI, Response, status
import hashlib
app = FastAPI()


@app.get("/auth")
def password_get(response: Response, password = None, password_hash = None):
    #password_hash = hashlib.sha512(("haslo").encode('utf-8'))
    #print(password_hash.hexdigest())
    #password_hash = hashlib.sha512(password.encode())
    password_without_spaces = password.replace(" ", "")
    if password_without_spaces is None or password_hash is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return response.status_code
    password_sha512 = hashlib.sha512(password_without_spaces.encode('utf-8')).hexdigest()
    if password_sha512 == password_hash:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response.status_code
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return response.status_code

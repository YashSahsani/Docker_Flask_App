# Docker_Flask_App
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Prerequisites
- Docker
- Git

## Setup 
```bash
# Get repository
$ git clone https://github.com/YashSahsani/Docker_Flask_App.git & cd Docker_Flask_App/

# Run application
$ docker compose up

App will run on http://127.0.0.1:5000
 ```
| Parameter | Example 
| - | - 
| `environment` | `localhost:5000`

## API Endpoints

```bash
$ Get User Information
$ curl http://{environment}//GetUserInfo?uid={UID}
$ # Example
$ curl http://{environment}/GetUserInfo?uid=1
```

```bash
$ # Create user 
$ data={"name":"{name}","age":{age},"city":"{city}"}
$ Encode data with JWT 
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"{encrypted with JWT}"}' http://{environment}/CreateUser
$ # Example
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYXJ5YSIsImFnZSI6MjAsImNpdHkiOiJOZXcgeW9yayJ9.HWv_0ILo0HvMoYlmX01L3rIFfKUYmFSzail0x-FDTC0"}' http://{environment}/CreateUser
```
```bash
$ Similarly other Endpoints are
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"{encrypted with JWT}"}' http://{environment}/EditUser/<uid>
$ # Example
$ curl curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYXJ5YSIsImFnZSI6MjAsImNpdHkiOiJOZXcgeW9yayJ9.HWv_0ILo0HvMoYlmX01L3rIFfKUYmFSzail0x-FDTC0"}' http://{environment}/EditUser/3
$ curl -X POST -H "Content-Type: application/json" -d '{"token":"{encrypted with JWT}"}' http://{environment}/DeleteUser/<uid>
```

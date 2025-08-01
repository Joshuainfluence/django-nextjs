from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # is not request.is_authenticated
    email: str = None



@api.get("/hello")
def hello(request):
    print(request)
    return("Hello world!")  

@api.get("me", response=UserSchema)
def me(request):
    return request.user
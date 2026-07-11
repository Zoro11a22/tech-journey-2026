class App:
    def __init__(self):
        self.routes = []
    
    def route(self, path, method="GET"):
        method = method.upper()

        def decorator(func):
            self.routes.append({
                "path": path,
                "method": method,
                "function": func
            })
            return func

        return decorator

    def get(self, path):
        return self.route(path=path, method="GET")

    def post(self, path):
        return self.route(path=path, method="POST")

    def dispatch(self, path, method):
        method = method.upper()

        for route in self.routes:
            if route["path"] == path and route["method"] == method:
                return route["function"]()

        return "404 Not Found"

app = App()

@app.get("/")
def home():
    return "Home"

@app.get("/users")
def get_users():
    return "All users"

@app.post("/users")
def create_user():
    return "User created"

@app.post("/login")
def login():
    return "Logged in"

for route in app.routes:
    print(f"{route['method']} {route['path']} -> {route['function'].__name__}")

print(app.dispatch("/", "GET"))
print(app.dispatch("/users", "GET"))
print(app.dispatch("/users", "POST"))
print(app.dispatch("/login", "POST"))
print(app.dispatch("/admin", "GET"))
from nursing_knowledge_ia_backend.routes.server.server import StartServer

def StartApp():
    app=StartServer()

    app.run(debug=True,port=8080)

if __name__ == '__main__':
    StartApp()

from nursing_knowledge_ia_backend.routes.server.server import StartServer
from nursing_knowledge_ia_backend.config.env import LoadEnv

def StartApp():
    LoadEnv()
    app=StartServer()

    app.run(debug=True,port=8080)

if __name__ == '__main__':
    StartApp()

from nursing_knowledge_ia_backend.routes.server.server import StartServer
from nursing_knowledge_ia_backend.config.env import GetDBConnection, GetDBName, LoadEnv
from nursing_knowledge_ia_backend.database.connection import InitConnection

def StartApp():
    LoadEnv()
    app=StartServer()
    InitConnection(GetDBConnection(),GetDBName())

    app.run(debug=True,port=8080)

if __name__ == '__main__':
    StartApp()

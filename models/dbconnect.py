from sqlalchemy import create_engine

def getEngine():

    url = 'housestack.crzf2jqpqelj.us-east-2.rds.amazonaws.com'
    username = 'admin'
    password = 'housestack'
    db = 'TEST'
    dbpath = f'mysql://{username}:{password}@{url}/{db}'

    engine = create_engine( dbpath , echo = True)

    return engine



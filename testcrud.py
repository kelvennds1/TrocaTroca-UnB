from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Base  # Assuming your SQLAlchemy models are defined in a separate module
from trocatroca0_orm import * 
from flask import Flask

app = Flask(__name__)

# Configure o banco de dados
engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# table_names = Base.metadata.tables.keys()

# for table_name in table_names:
#     print(f"Table Name: {table_name}")
#     table = Base.metadata.tables[table_name]
#     for column in table.c:
#         print(f"Column: {column.name}, Type: {column.type}")
#     print("---------------")

Item.metadata.create_all(engine)

table_names = Item.metadata.tables.keys()

for table_name in table_names:
    print(f"Table Name: {table_name}")
    table = Item.metadata.tables[table_name]
    for column in table.c:
        print(f"Column: {column.name}, Type: {column.type}")
    print("---------------")


# if __name__ == '__trocatroca_novo_db_210723__':
#     app.run(debug=False, host='0.0.0.0')

if __name__ == '__testcrud__':
    app.run()
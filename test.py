from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import *
a=get_all_products(Session(engine))
for i in a:
    print(i['product_Name'])
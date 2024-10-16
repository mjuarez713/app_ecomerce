# catalogo/app.py
from app import create_app, db

app = create_app()
app.app_context().push()

if __name__ == '__main__':
  db.create_all()
  app.run(host="0.0.0.0", port=5000)

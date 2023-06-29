# API-DJANGO
Cosas a tener en cuenta:
1. Crear un entorno virtual.
2. Activar el entorno virtual.
3. Instalar: pip install django psycopg2-binary python-decouple djangorestframework drf-yasg
4. Crear un archivo .env a la altura de requirements.txt con los siguientes datos:
  SECRET_KEY=django-insecure-d7l#(*kb8*e)js$l(k1#(jidr+=3rqdq3iu(#&204su8=mg-*i
  DEBUG=True
  ENGINE=django.db.backends.postgresql
  PGSQL_HOST=localhost
  PGSQL_USER=postgres
  PGSQL_PASSWORD=1234
  PGSQL_DATABASE=COLEGIO
  PGSQL_PORT=5433
5. Crear una base de datos "COLEGIO" en PostgreSQL
6. Correr la migraciones

#### Description
Two containers are set up with docker-compose. On start up the ETL will be launched and fill the database with the data from API.


#### Run the app with docker compose
```
docker-compose build --no-cache
docker-compose up --force-recreate
```

### 
After containers are started there should be 4 tables in the postgres database:
- publications_counter
- launches
- missions
- rockets
- ships

The table "publications_counter" is a desired data mart.

Check out the tables by running:
```
PGPASSWORD=postgres psql \
   --host=0.0.0.0 \
   --port=5432 \
   --username=postgres \
   --dbname=postgres \
   -c 'select * from publications_counter'
```

FROM postgres:9.6-alpine
COPY static/data.sql /sql
RUN psql -d $POSTGRES_DB -U $POSTGRES_USER -p 5432 -a -w -f /sql/data.sql

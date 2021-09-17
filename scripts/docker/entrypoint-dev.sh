#!/bin/sh

until psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB} -c '\l'; do
    echo -e "\e[34m >>> Postgres is unavailable - sleeping \e[97m"
    sleep 1
done

echo -e "\e[32m >>> Postgres is up - continuing \e[97m"

echo -e "\e[34m >>> Running migrations \e[97m"
alembic upgrade head
if [ $? -eq 0 ]; then
    echo -e "\e[32m >>> Migration successful \e[97m"
else
    echo -e "\e[31m >>> Migration failed \e[97m"
    exit 1
fi

echo -e "\e[34m >>> Starting the server \e[97m"
uvicorn serverctl.main:app --host 0.0.0.0 --port 8000 --reload

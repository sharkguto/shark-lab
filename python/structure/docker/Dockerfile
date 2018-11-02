FROM python:3.6-stretch

RUN mkdir -p /opt/apps/
WORKDIR /opt/apps/

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY dercypy ./dercypy

COPY ./dercypy/static static 

EXPOSE 5000

#ENTRYPOINT ["python3"]

ENTRYPOINT ["python3","-m", "dercypy"]
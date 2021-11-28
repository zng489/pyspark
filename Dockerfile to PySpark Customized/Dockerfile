FROM jupyter/pyspark-notebook:latest

RUN mkdir -p /home/jovyan/work
WORKDIR /home/jovyan/work

RUN pip install --upgrade pip

#COPY requirements_docker.txt ./
#RUN pip install -r requirements_docker.txt

RUN pip install jupyterthemes

EXPOSE 8888

#ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]


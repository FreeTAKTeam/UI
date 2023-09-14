FROM python:3.8

ENV \
    TARGET_PROJECT_DIR=/fts-ui \
    LOCAL_SRC_DIR=./FreeTAKServer-UI \ 
    TARGET_SRC_DIR=/fts-ui/FreeTAKServer-UI \
    TARGET_DATA_BASE_DIR=/opt/fts

WORKDIR $TARGET_PROJECT_DIR
COPY . $TARGET_PROJECT_DIR

RUN pip3 install -e $TARGET_PROJECT_DIR
RUN pip3 install -r $TARGET_PROJECT_DIR/requirements.txt
RUN pip3 install -r $TARGET_PROJECT_DIR/requirements-pgsql.txt


# WebUIPort
EXPOSE 5000
# WebMapsPort
EXPOSE 8000

ENTRYPOINT ["nohup", "python3", "./FreeTAKServer-UI/run.py"]

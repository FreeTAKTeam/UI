FROM python:3.11

RUN groupadd -r freetak && useradd -m -r -g freetak freetak
USER freetak

WORKDIR app/

COPY --chown=freetak:freetak . ./

# Install pre-reqs then the base FTS
ENV PATH /home/freetak/.local/bin:/home/freetak/.local/lib:$PATH
RUN pip3 install -r requirements.txt
RUN pip3 install /app
WORKDIR /home/freetak/.local/lib/python3.11/site-packages/FreeTAKServer-UI/

expose 5000

ENTRYPOINT ["python", "run.py"]
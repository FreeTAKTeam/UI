FROM python:3.11

RUN groupadd -r freetak && useradd -m -r -g freetak freetak

RUN mkdir -p /home/freetak/data && chown -R freetak:freetak /home/freetak/data

USER freetak
WORKDIR /usr/src/app

# Install pre-reqs then the base FTS
ENV PATH /home/freetak/.local/bin:/home/freetak/.local/lib:$PATH

COPY --chown=freetak:freetak --chmod=774 . ./
RUN ls
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .


# Get a way to edit the configuration from outside the container
WORKDIR /home/freetak/.local/lib/python3.11/site-packages/FreeTAKServer-UI/
RUN mv config.py config.bak

EXPOSE 5000/tcp
VOLUME /home/freetak/data
CMD ["/usr/src/app/docker-run.sh"]
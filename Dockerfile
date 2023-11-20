FROM python:3.11

RUN groupadd -r freetak && useradd -m -r -g freetak freetak

RUN mkdir -p /home/freetak/data && chown -R freetak:freetak /home/freetak/data && chmod 777 -R /home/freetak/data && chmod g+s /home/freetak/data
RUN ln -s /opt/FTSServer-UI.db /home/freetak/data/FTSServer-UI.db

USER freetak
WORKDIR /home/freetak

# Install pre-reqs then the base FTS
ENV PATH /home/freetak/.local/bin:/home/freetak/.local/lib:$PATH

COPY --chown=freetak:freetak --chmod=774 . ./
RUN pwd && ls

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .


# Provide a way to edit the configuration from outside the container
RUN mv /home/freetak/FreeTAKServer-UI/config.py /home/freetak/FreeTAKServer-UI/config.bak

EXPOSE 5000/tcp
VOLUME /home/freetak/data
CMD ["/home/freetak/docker-run.sh"]
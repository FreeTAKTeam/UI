# Pull python 3.11 because that is our latest target
FROM python:3.11-slim

#RUN apt-cache policy sqlite3
#RUN apt-get install -y sqlite3

# Add non-root user to limit privilege to minimum required to function
#RUN adduser --disabled-password freetak

RUN useradd --system --create-home --shell /bin/bash freetak
#RUN chown -R freetak:root /opt
#RUN chmod -R 777 /opt
#VOLUME /opt

USER freetak

# Move to non-root user's home directory as that should be the only place it has permission
WORKDIR /home/freetak/
ENV PATH /home/freetak/.local/bin:/home/freetak/.local/lib:$PATH

COPY --chown=freetak:freetak --chmod=774 . ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

# When container is run, run our startup script
#ENTRYPOINT ls
CMD ["/home/freetak/docker-run.sh"]
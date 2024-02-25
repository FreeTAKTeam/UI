# Pull python 3.11 because that is our latest target
FROM python:3.11-slim

# Add non-root user to limit privilege to minimum required to function
#RUN adduser --disabled-password --home /home/freetak freetak
RUN useradd --system --create-home --shell /bin/bash freetak
USER freetak

# Move to non-root user's home directory as that should be the only place it has permission
WORKDIR /home/freetak/
ENV PATH /home/freetak/.local/bin:/home/freetak/.local/lib:$PATH

COPY --chown=freetak:freetak --chmod=774 . ./

RUN pip install --ignore-installed PyYAML --no-cache-dir -r requirements.txt
RUN pip install -e .

# When container is run, run our startup script
CMD ["/home/freetak/docker-run.sh"]
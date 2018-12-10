FROM alephdata/memorious:latest

RUN pip install --upgrade -q psycopg2-binary


COPY . /ocds/
RUN pip install -q -e /ocds

ENV MEMORIOUS_CONFIG_PATH=/ocds/crawlers/config \
    MEMORIOUS_DEBUG=true
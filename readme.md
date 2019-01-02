# OCDS Memorious Crawlers

This repo contains crawlers for OCDS data from various publishers, using the [memorious](https://github.com/alephdata/memorious) crawler framework. 

Initially sources are based on those in [OCDS Kingfisher](https://github.com/open-contracting/kingfisher).

## Storage

At this time crawlers dump downloaded JSON to disc in the `data` directory.

## Running with docker

NB. This is mostly note-to-self at this point.

```
(host) sudo docker build -t ods/crawlers .

(host) sudo docker run -it -v /home/rhiaro/Documents/code/ocds-memorious-crawlers/:/ocds -p 4000:4000 --name crawlers ods/crawlers /bin/bash
```

Do CLI stuff:

```
(crawlers) memorious list

(crawlers) memorious run ca_buyandsell
```

Fire up the UI:

```
(crawlers) python memorious/ui/views.py
```
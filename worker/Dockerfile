FROM public.ecr.aws/docker/library/python:3.10-alpine3.13
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /web
WORKDIR /web
COPY ./docker/requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./web /web/
RUN ["chmod", "+x", "/web/scripts/docker-entrypoint-worker.sh"]
ENTRYPOINT ["/web/scripts/docker-entrypoint-worker.sh"]
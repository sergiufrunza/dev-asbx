FROM public.ecr.aws/docker/library/nginx:1.21-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d
COPY ../../web/static /home/app/web/static/
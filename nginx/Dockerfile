FROM public.ecr.aws/docker/library/nginx:1.21-alpine
EXPOSE 80
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d
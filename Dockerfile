FROM public.ecr.aws/nginx/nginx:stable-alpine-slim
COPY satori_help/docs /usr/share/nginx/html
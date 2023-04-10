FROM node:lts-alpine as build-stage
WORKDIR /app
COPY /vue3_webfrontend/package.json /app/
COPY /vue3_webfrontend/yarn.lock /app/
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && npm config set registry https://registry.npm.taobao.org && yarn
COPY /vue3_webfrontend/ /app/
RUN yarn build


FROM python:3.8
WORKDIR /usr/src/app
COPY --from=build-stage /app/dist/ /usr/src/app/dist
COPY /webbackend/requirements.txt .
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY /webbackend/ .
ENV ENV=prod

EXPOSE 1101
CMD python main.py 
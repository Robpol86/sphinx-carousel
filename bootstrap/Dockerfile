FROM node:17 as base
ENTRYPOINT /bin/bash
SHELL ["/bin/bash", "-c"]

FROM base as build
WORKDIR /work
COPY package.json ./
RUN npm install
COPY .browserslistrc ./
COPY banner.js postcss.config.js rollup.config.js ./build/
COPY bootstrap-carousel.scss ./scss/
COPY index.esm.js index.umd.js ./js/
RUN npm run dist

#FROM base as validate
#WORKDIR /work
#ENV BS_VER=5.1.3
#RUN wget "https://github.com/twbs/bootstrap/releases/download/v$BS_VER/bootstrap-$BS_VER-dist.zip"
#RUN unzip bootstrap-$BS_VER-dist.zip && mv bootstrap-$BS_VER-dist precompiled
#COPY --from=build /work/dist ./compiled
#RUN diff --color=always -u {pre,}compiled/css/bootstrap-carousel.css
#RUN diff --color=always -u {pre,}compiled/js/bootstrap-carousel.js

FROM base as final
WORKDIR /dist
COPY --from=build /work/dist/css/* /work/dist/js/* ./

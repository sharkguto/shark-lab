from alpine:3.7

WORKDIR /jaspion

add server .


run apk add --no-cache --update \
    bash \
    python3 \
    python3-dev \
    sudo \
    curl \
    openssl \
    tar \
    gawk \
    make \
    g++ \
    libffi \
    busybox \
    busybox-extras \
    ca-certificates && \
    curl -Ls https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-2.27-r0.apk > /tmp/glibc-2.27.r0.apk && \
    apk add --allow-untrusted /tmp/glibc-2.27.r0.apk

run sudo python3 -m pip install -r /jaspion/requeriments.txt

CMD [ "python3","/jaspion/app.py"]
FROM alpine:3.9.3
COPY start.sh /start.sh
RUN apk update \
    && apk add jq \
    && apk add gnupg \
    && wget https://dist.ipfs.io/go-ipfs/v0.11.0/go-ipfs_v0.11.0_linux-amd64.tar.gz \
    && tar -xvzf go-ipfs_v0.11.0_linux-amd64.tar.gz \
    && cd go-ipfs \
    && apk add --no-cache bash \    
    && bash install.sh \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
    && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.34-r0/glibc-2.34-r0.apk \
    && apk add glibc-2.34-r0.apk
ENTRYPOINT [ "./start.sh" ]
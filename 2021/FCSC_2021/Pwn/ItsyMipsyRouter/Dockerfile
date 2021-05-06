FROM debian:buster-slim
RUN apt update
RUN apt install -yq socat qemu-user libc6-mips64-cross
RUN apt clean
RUN rm -rf /var/lib/apt/lists/

WORKDIR /app
COPY ./mipsy ./
RUN rm /etc/ld.so.cache

EXPOSE 4000
CMD socat tcp-listen:4000,reuseaddr,fork exec:"qemu-mips64 -L /usr/mips64-linux-gnuabi64 ./mipsy"

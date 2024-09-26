FROM alpine:3.18

RUN apk update && apk add --no-cache bash neofetch

CMD ["/bin/bash"]

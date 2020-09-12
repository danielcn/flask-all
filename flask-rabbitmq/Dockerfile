FROM rabbitmq:3.7

WORKDIR /usr/local/bin/
ADD ./init.sh .
RUN chmod +x ./init.sh

CMD ["./init.sh"]
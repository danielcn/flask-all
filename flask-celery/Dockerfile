FROM rabbitmq:3.8.3

MAINTAINER "Daniel Nascimento"

RUN mkdir -p /etc/bash_completion.d/ \
	&& apt-get update && apt-get install -y --no-install-recommends \
		python \
		bash-completion \
	&& rm -rf /var/lib/apt/lists/*

COPY rabbitmqadmin /usr/local/bin/rabbitmqadmin

ENV HOME /root

RUN chmod 755 /usr/local/bin/rabbitmqadmin; sync \
	&& rabbitmqadmin --bash-completion > /etc/bash_completion.d/rabbitmqadmin \
	&& echo "source /etc/bash_completion.d/rabbitmqadmin" >> ~/.bashrc

CMD [ "/bin/bash" ]
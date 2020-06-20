FROM centos:7

RUN yum -y update
RUN yum clean all

SHELL ["/bin/bash", "-c"]

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
RUN source /root/.bashrc && \
nvm install stable && \
# npm i -g express-generator && \
# npm i -g forever

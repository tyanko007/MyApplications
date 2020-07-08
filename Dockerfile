FROM centos:7

RUN yum -y update
RUN yum clean all

# python36に必要なパッケージ群
RUN yum install -y bzip2 bzip2-devel gcc gcc-c++ make openssl-devel readline-devel zlib-devel wget curl unzip vim epel-release git && yum install -y tig jq vim-enhanced bash-completion net-tools bind-utils

# pythonが含まれるrpmのダウンロード
RUN yum install -y https://repo.ius.io/ius-release-el7.rpm

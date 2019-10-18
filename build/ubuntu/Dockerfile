FROM ubuntu:17.10
MAINTAINER \
[Hatchpay <support@hatch.ga>]
RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get -y install libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool libpython3-all-dev python3.6-dev python3-pip git cmake \
 && pip3 install virtualenv \
 && cd ~ \
 && mkdir hmt \
 && cd hmt \
 && virtualenv -p python3 venv \
 && . venv/bin/activate \
 && pip install --upgrade setuptools \
 && git clone https://github.com/hatchpay/hatch-masternode-tool \
 && cd hatch-masternode-tool/ \
 && pip install -r requirements.txt \
 && cd ~/hmt \
 && echo "#!/bin/sh" | tee build-hmt.sh \
 && echo "cd ~/hmt" | tee -a build-hmt.sh \
 && echo ". venv/bin/activate" | tee -a build-hmt.sh \
 && echo "cd hatch-masternode-tool" | tee -a build-hmt.sh \
 && echo "git fetch --all" | tee -a build-hmt.sh \
 && echo "git reset --hard origin/master" | tee -a build-hmt.sh \
 && echo "pip install -r requirements.txt" | tee -a build-hmt.sh \
 && echo "pyinstaller --distpath=../dist/linux --workpath=../dist/linux/build hatch_masternode_tool.spec" | tee -a build-hmt.sh \
 && echo "cd .." | tee -a build-hmt.sh \
 && chmod +x build-hmt.sh

CMD ~/hmt/build-hmt.sh

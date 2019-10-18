FROM fedora
MAINTAINER \
[Hatchpay <support@hatch.ga>]
RUN yum update -y \
 && yum group install -y "Development Tools" "Development Libraries" \
 && yum install -y redhat-rpm-config python3-devel libusbx-devel libudev-devel cmake gcc-c++ \
 && yum remove -y gmp-devel \
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
 && set +H \
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

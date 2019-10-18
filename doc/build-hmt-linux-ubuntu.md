## Building the Hatch Masternode Tool executable on Ubuntu Linux

### Method based on physical or virtual linux machine

An Ubuntu distribution with Python 3.6 is required to build HMT. This example uses Ubuntu 17.10, which comes with an appropriate version installed by default. You can verify the Python version by typing:

```
python3 --version
```

You should see a response similar to the following:

  `Python 3.6.4`

After making sure that you have the correct Python version, execute the following commands from the terminal:

```
[hmt@ubuntu /]# sudo apt-get update
[hmt@ubuntu /]# sudo apt-get -y upgrade
[hmt@ubuntu /]# sudo apt-get -y install libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool libpython3-all-dev python3.6-dev python3-pip git cmake
[hmt@ubuntu /]# sudo pip3 install virtualenv
[hmt@ubuntu /]# sudo pip3 install --upgrade pip
[hmt@ubuntu /]# cd ~
[hmt@ubuntu /]# mkdir hmt && cd hmt
[hmt@ubuntu /]# virtualenv -p python3.6 venv
[hmt@ubuntu /]# . venv/bin/activate
[hmt@ubuntu /]# pip install --upgrade setuptools
[hmt@ubuntu /]# git clone https://github.com/hatchpay/hatch-masternode-tool
[hmt@ubuntu /]# cd hatch-masternode-tool/
[hmt@ubuntu /]# pip install -r requirements.txt
[hmt@ubuntu /]# pyinstaller --distpath=../dist/linux --workpath=../dist/linux/build hatch_masternode_tool.spec
```

The following files will be created once the build has completed successfully:

* Executable: `~/hmt/dist/linux/HatchMasternodeTool`
* Compressed executable: `~/hmt/dist/all/HatchMasternodeTool_<verion_string>.linux.tar.gz`


### Method based on Docker

This method uses a dedicated **docker image** configured to carry out an automated build process for *Hatch Masternode Tool*. The advantage of this method is its simplicity and the fact that it does not make any changes in the list of installed apps/libraries on your physical/virtual machine. All necessary dependencies are installed inside the Docker container. The second important advantage is that compilation can also be carried out on Windows or macOS (if Docker is installed), but keep in mind that the result of the build will be a Linux executable.

> **Note: Skip steps 3 and 4 if you are not performing this procedure for the first time (building a newer version of HMT, for example)**

#### 1. Create a new directory
We will refer to this as the *working directory* in the remainder of this documentation.

#### 2. Open the terminal app and `cd` to the *working directory*

```
cd <working_directory>
```

#### 3. Install the *hatchpay/build-hmt:ubuntu* Docker image

Skip this step if you have done this before. At any time, you can check whether the required image exists in your local machine by issuing following command:

```
docker images hatchpay/build-hmt:ubuntu
```

The required image can be obtained in one of two ways:

**Download from Docker Hub**

Execute the following command:

```
docker pull hatchpay/build-hmt:ubuntu
```

**Build the image yourself, using the Dockerfile file from the HMT project repository.** 

* Download the https://github.com/hatchpay/hatch-masternode-tool/blob/master/build/ubuntu/Dockerfile file and place it in the *working directory*
* Execute the following command:
```
docker build -t hatchpay/build-hmt:ubuntu .
```

#### 4. Create a Docker container

A Docker container is an instance of an image (similar to how an object is an instance of a class in the software development world), and it exists until you delete it. You can therefore skip this step if you have created the container before. To easily identify the container, we give it a specific name (hmtbuild) when it is created so you can easily check if it exists in your system.

```
docker ps -a --filter name=hmtbuild --filter ancestor=hatchpay/build-hmt:ubuntu
```
Create the container:

``` 
mkdir -p build
docker create --name hmtbuild -v $(pwd)/build:/root/hmt/dist -it hatchpay/build-hmt:ubuntu
```

#### 5. Build the Hatch Masternode Tool executable

```
docker start -ai hmtbuild
```

When the command completes, compiled binary can be found in the 'build' subdirectory of your current directory.

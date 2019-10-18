## Building the Hatch Masternode Tool executable on macOS

You can build Hatch Masternode Tool for macOS by opening the Terminal app and running the following commands:

* Install *Homebrew*:

  ```
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

  Installation takes about 5 minutes to complete.

* Install *Python 3*:

  ```
  brew install python3
  ```

* After the installation process completes, make sure that the Python version installed is 3.6 or newer. HMT won't compile on older versions of Python, or even older versions of Python 3:

  ```
  python3 --version
  ```

  You should see a response similar to the following:

  `Python 3.6.4`

* Install *virtualenv*:

  ```
  pip3 install virtualenv
  ```

* Create a Python virtual environment for HMT:

  ```
  cd ~
  mkdir projects
  mkdir projects/virtualenvs
  cd projects/virtualenvs
  virtualenv -p python3 hmt
  ```

* Activate the new virtual environment:

  ```
  source hmt/bin/activate
  ```

* Download the HMT source from GitHub:

  ```
  cd ~/projects
  git clone https://github.com/hatchpay/hatch-masternode-tool
  ```

* Install the HMT Python requirements:

  ```
  cd hatch-masternode-tool
  pip install -r requirements.txt
  ```

* Build the HMT executable:

  ```
  pyinstaller --distpath=../dist/mac --workpath=../build/mac hatch_masternode_tool.spec
  ```


Once the build has completed successfully, a compressed macOS executable file will be created in the ***~/projects/dist/all*** directory. An uncompressed app package (*HatchMasternodeTool.app*) can be found in the ***~/projects/dist/mac*** directory.
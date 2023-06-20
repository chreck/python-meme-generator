# In general

If you are having issues please run the application with python 3.9.

# Issues

Several issues I faced with the Udacity workspace with python 3.6 by creating the venv with `python -m venv venv` . Because I got the error:

`Error: Command '['/workspace/home/python-meme-generator/venv/bin/python', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.`

Using a Macintosh with a M1 CPU let not run python 3.6 anymore so I decided to go with python version 3.9 .

# Run application with python 3.6 and 3.9

I tried several steps to install python 3.6 on the machine macOS machine but all failed. Also installing a newer version of python like 3.9 in the udacity workspace failed in the end.

## pipenv - failed

`python -m pip install --upgrade pip`
`pip install pipenv`
`pipenv install`
`pipenv shell`

Pipenv shell fails with `termios.error: (25, 'Inappropriate ioctl for device')`

## python 3.9 - failed

Follow the instructions at https://prodisup.com/posts/2021/03/installing-python3.9-on-ubuntu-16.04-xenial/

`apt-get update`
`apt-key adv --refresh-keys --keyserver keyserver.ubuntu.com`
`apt-get -y install software-properties-common`
`add-apt-repository ppa:deadsnakes/ppa`
`apt-get update`

## python 3.9 manually - failed

```shell
sudo apt update

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget libbz2-dev libssl-dev liblzo2-dev libpam0g-dev
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz

tar -xf Python-3.9.7.tgz
./configure --enable-optimizations
make -j $(nproc)
make install
```

Failed because of OpenSSL version 1.1.1+ was missing for python 3.9

## pyenv

This is installation steps are tested on an Ubuntu 16.4 Xenial

`curl https://pyenv.run | bash`

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

Install python 3.9, this may take a while...

`pyenv install 3.9`

Select 3.9 as default

`pyenv global 3.9`

This could work but the workspace reset it all afterwards.

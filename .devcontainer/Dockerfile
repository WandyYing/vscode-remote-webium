#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

FROM python:3.7.6-buster

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ARG YOUR_ENV
ENV YOUR_ENV=${YOUR_ENV}

# This Dockerfile adds a non-root user with sudo access. Use the "remoteUser"
# property in devcontainer.json to use it. On Linux, the container user's GID/UIDs
# will be updated to match your local UID/GID (when using the dockerFile property).
# See https://aka.ms/vscode-remote/containers/non-root-user for details.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Uncomment the following COPY line and the corresponding lines in the `RUN` command if you wish to
# include your requirements in the image itself. It is suggested that you only do this if your
# requirements rarely (if ever) change.
# COPY requirements.txt /tmp/pip-tmp/

# Chanage to aliyun mirrors
# 更新apt-get源, aliyun 会导致apt-utils dialog的错误
# RUN echo "deb https://mirrors.aliyun.com/debian/ stretch main non-free contrib" > /etc/apt/sources.list && \
#     echo "deb-src https://mirrors.aliyun.com/debian/ stretch main non-free contrib" >> /etc/apt/sources.list  && \
#     echo "deb https://mirrors.aliyun.com/debian-security stretch/updates main" >> /etc/apt/sources.list && \
#     echo "deb-src https://mirrors.aliyun.com/debian-security stretch/updates main" >> /etc/apt/sources.list && \
#     echo "deb https://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list && \
#     echo "deb-src https://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list && \
#     echo "deb https://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list && \
#     echo "deb-src https://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list

# Configure apt and install packages
RUN apt-get update && apt-get upgrade -y && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git iproute2 procps lsb-release \
    #y
    # Install pylint
    && pip --disable-pip-version-check --no-cache-dir install pylint \
    #
    # Update Python environment based on requirements.txt
    # && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    # && rm -rf /tmp/pip-tmp \
    #
    # Create a non-root user to use if preferred - see https://aka.ms/vscode-remote/containers/non-root-user.
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support for the non-root user
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    #
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

#========================
# Miscellaneous packages
# Includes minimal runtime used for executing non GUI Java programs
#========================
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    ca-certificates \
    sudo \
    unzip \
    wget \
    curl \
  && rm -rf /var/lib/apt/lists/* 

#============================================
# Google Chrome
#============================================
# can specify versions by CHROME_VERSION;
#  e.g. google-chrome-stable=53.0.2785.101-1
#       google-chrome-beta=53.0.2785.92-1
#       google-chrome-unstable=54.0.2840.14-1
#       latest (equivalent to google-chrome-stable)
#       google-chrome-beta  (pull latest beta)
#============================================
ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*


#============================================
# Chrome webdriver
#============================================
# can specify versions by CHROME_DRIVER_VERSION
# Latest released version will be used by default
#============================================
ARG CHROME_DRIVER_VERSION="latest"
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo $(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else echo $CHROME_DRIVER_VERSION; fi) \
  && echo "Using chromedriver version: "$CD_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CD_VERSION \
  && sudo ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/bin/chromedriver

#=================================
# Chrome Launch Script Wrapper
#=================================
COPY wrap_chrome_binary /opt/bin/wrap_chrome_binary
RUN /opt/bin/wrap_chrome_binary

# Install poetry
# USER vscode
# ENV PATH=${HOME}/.local/bin:${PATH}
# curl has some issue with local user, "cannot found poetry"
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
RUN pip3 install poetry
ENV PATH=/root/.poetry/bin/:$PATH
# RUN pip3 install --user poetry
# RUN PATH=${HOME}/.local/bin:${PATH}

# if first run with blank project, run below in Terminal in VSCode.
# poetry new ${your_project_name}
# poetry install 
# poetry add ${package}
# ==============================================
# create application directory
RUN sudo mkdir /app
WORKDIR /app
# ==============================================
# if has poetry project, execute below commad
# ONBUILD COPY pyproject.* .
# # install dependencies:
# ONBUILD RUN poetry install -n
# ==============================================
# # Option: Two(Recommend)
ARG YOUR_ENV
ENV YOUR_ENV=${YOUR_ENV}
COPY webium/poetry.lock webium/pyproject.toml /app/
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# USER vscode
# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog


FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y
RUN apt install -y \
	build-essential \
	curl \
	gnupg2 \
	lsb-release \
	net-tools \
	wget \
	python3-pip \
	vim \
	git \
	openssh-server

# clone used git
RUN mkdir ~/.repos
RUN git clone https://github.com/bonohub13/vim_settings ~/.repos/vim_settings
RUN git clone https://github.com/morhetz/gruvbox ~/.repos/gruvbox
RUN git clone https://github.com/bonohub13/my_led ~/.repos/my_led

# vim settings
RUN mkdir ~/.vim
RUN mv ~/.repos/gruvbox/colors ~/.vim
RUN mv ~/.repos/vim_settings/.vimrc ~/

# ROS2 settings
ADD init_run.bash /bin/init_run.bash
RUN mv /bin/init_run.bash ~/

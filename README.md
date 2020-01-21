# myled_in_ROS2

## Instructions
- __First__
	- This is using my former repository, so you'd want to clone that as well
		- URL: https://github.com/bonohub13/my_led.git

	- If you're using Docker for the environment of ROS2, the whole procedure is automated in the Dockerfile in this repository

- Procedures on installing ROS2 on your home environment or in Docker containers
	- home environment
		- run the <i>init_run.bash</i> __with sudo__ ~~[updated January 18th, 2020]~~ [updated Jan 21st, 2020]
	- Docker containers
		- build the Dockerfile __INSIDE__ of the directory of where the Dockerfile is located
			- $ sudo docker build -t <whatever tag name you'd like> ./
		- make a Docker container out of the built Docker image
		- run the <i>init_run.bash</i>

## Fair Notice
- The ROS2 installer in this repository only installs the basic components (No GUIs)
	- If you want the ROS2 desktop version, go to the following link
		- link: https://github.com/ryuichiueda/ros2_setup_scripts_Ubuntu18.04_desktop.git

## Updates
- January 17th, 2020
	- changed init_run.bash file to change the installation based on the $HOME user
		- added sudo for non-root users

- January 21st, 2020
	- since the user based installation did NOT work, I fixed it back to the original installer which needs sudo permit unless run on root user (root Not recommended for native environment!)

## Special Thanks to...
- Ryuichi Ueda
	- URL: https://github.com/ryuichiueda/ros2_setup_scripts_Ubuntu18.04_desktop.git

## Referenced
- Yutaka Kondo
	- 近藤豊 (2019) "ROS2ではじめよう 次世代ロボットプログラミング" 技術評論社
		- URL: https://www.amazon.co.jp/dp/B07W6DX9MW/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1

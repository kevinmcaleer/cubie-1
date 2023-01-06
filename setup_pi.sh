# check for updates and apply them
echo "check for updates and apply them"
sudo apt update
sudo apt upgrade -y

# get Cubie-1 files
echo "get Cubie-1 files"
git clone https://github.com/kevinmcaleer/cubie-1

# Get official ROS docker images
echo "Get official ROS docker images"
git clone https://www.github.com/osrf/docker_images

# Remove any existing docker installation
echo "Remove any existing docker installation"
sudo apt-get purge docker-ce docker-ce-cli containerd.io -y

# Get docker and install
echo "Get docker and install"
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh 
./get-docker.sh

"Build ROS-Base"
cd docker_images/ros/humble/ubuntu/jammy/ros-base
docker build -t ros2 .

echo "done."
echo "type `docker run -it -v /home/kev/cubie-1:/ros2 ros2` to run ros2"
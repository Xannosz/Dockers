docker rm -f bluequeen
docker pull xannosz/bluequeen:latest
docker run -v /var/lib/docker/containers:/var/lib/docker/containers -v /persist:/persist -v /var/run/docker.sock:/var/run/docker.sock -p 3500:8888 --name bluequeen -d xannosz/bluequeen:latest
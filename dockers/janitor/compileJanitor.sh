docker run -v /c/Users/kissa/git/Dockers/dockers/janitor:/janitor -v /var/run/docker.sock:/var/run/docker.sock -ti --entrypoint bash data61/magda-builder-docker:latest

docker buildx build -t xannosz/janitor:3-arm64 -t xannosz/janitor:latest-arm64 --push --platform=linux/arm64 .
docker buildx build -t xannosz/janitor:3-amd64 -t xannosz/janitor:latest-amd64 --push --platform=linux/amd64 .
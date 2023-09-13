
docker-rebuild:
	docker-compose down
	git pull origin dev
	docker rmi -f $(docker images -aq)
	docker-compose up -d 


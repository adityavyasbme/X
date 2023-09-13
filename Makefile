
docker-rebuild:
	docker-compose down
	git pull origin dev
	docker image rm x_fastapi
	docker image rm x_streamlit
	docker-compose up -d 


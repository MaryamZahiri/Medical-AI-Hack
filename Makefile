docker_up_local:
	docker-compose -f docker-compose.local.yaml up -d --build

docker_down_local:
	docker-compose -f docker-compose.local.yaml down

ngrok_start:
	ngrok start --config confs/local/ngrok.yaml --all
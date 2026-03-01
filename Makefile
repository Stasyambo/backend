IMAGE=backend:latest

build:
	docker build -t $(IMAGE) .

scan:
	trivy image $(IMAGE)

deploy:
	kubectl apply -f k8s/

all: build scan deploy

requirements: ## install development environment requirements
	pip install -r requirements.txt

config: requirements
	@echo "-------------------------"
	@echo "Your environment is ready"
	@echo "Now run: make run"

run:
	python manage.py runserver 0.0.0.0:8000
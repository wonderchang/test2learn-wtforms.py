TEST ?=

workspace = $(PWD)
image = test2learn-python-wtforms

build:
	docker build -t $(image) .

define docker_run
	docker run --rm --interactive --tty \
		--volume $(workspace):/workspace \
		--env PYTHONDONTWRITEBYTECODE=1 \
		--env TEST=$(TEST) \
		$(image) $(1)
endef

shell:
	$(call docker_run,/bin/bash)

test:
	$(call docker_run,tox)

clean:
	docker rmi -f $(image)

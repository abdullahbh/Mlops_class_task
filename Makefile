# Makefile

.PHONY: test install

test:
	pytest test.py

install:
	pip3 install -r requirements.txt

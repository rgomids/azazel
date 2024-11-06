.PHONY: all build run clean

# Nome do binário que será gerado
BINARY_NAME = azazel-voice-server

# Diretório dos fontes
SRC = .

all: build

build:
	go build -o $(BINARY_NAME) $(SRC)/main.go

run: build
	./$(BINARY_NAME)

clean:
	rm -f $(BINARY_NAME)

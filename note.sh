#!/bin/bash
if [ -z "$1" ]; then
	    echo "Por favor, forneça uma anotação."
	        exit 1
fi

# Adiciona a data e a anotação ao arquivo ~/notes/notes.txt
echo -e "$(date)\n$1\n~~~~~~~~~~~~" >> ~/notes/notes.txt

echo "Anotação salva com sucesso"

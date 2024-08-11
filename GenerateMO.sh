#!/bin/bash
# Works on Windows in a Git Bash Terminal
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	MO_FILE="${PO_FILE/.po/.mo}"
	pybabel compile -i "$PO_FILE" -o "$MO_FILE"
done
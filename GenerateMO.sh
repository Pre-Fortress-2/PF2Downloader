#!/bin/bash
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	MO_FILE="${PO_FILE/.po/.mo}"
	pybabel -i "$PO_FILE" -o "$MO_FILE"
done
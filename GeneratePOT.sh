#!/bin/sh
POT_FILE=locale/pf2-downloader.pot
xgettext --package-name=pf2-downloader --keyword=_ --keyword=_N:1,2 -l python -o "$POT_FILE" *.py
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	msgmerge -U "$PO_FILE" "$POT_FILE"
done

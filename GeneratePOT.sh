#!/bin/bash
POT_FILE=locale/pf2-downloader.pot
pybabel extract --project=pf2-downloader --keywords=_ --keywords=_N:1,2 -o "$POT_FILE" *.py
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	LOCALE=${PO_FILE#"locale/"}; LOCALE=${LOCALE%"/LC_MESSAGES/"*.po}
	pybabel update -i "$POT_FILE" -o "$PO_FILE" -l "$LOCALE"
done
	
#!/bin/bash
GAME=pf2
POT_FILE=locale/$GAME-downloader.pot
pybabel extract --project=$GAME-downloader --keywords=_ --keywords=_N:1,2 -o "$POT_FILE" *.py
for PO_FILE in locale/*/LC_MESSAGES/*.po
do
	LOCALE=${PO_FILE#"locale/"}; LOCALE=${LOCALE%"/LC_MESSAGES/"*.po}
	pybabel update -i "$POT_FILE" -o "$PO_FILE" -l "$LOCALE"
done
	
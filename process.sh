#!/bin/bash
##counter=100
for value in {100..500}
do
    python3 detect.py object-localization document-$value.jpg
    ##echo $value
done

echo All done now

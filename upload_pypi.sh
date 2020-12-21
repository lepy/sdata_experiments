#!/bin/bash
cd ~/projects/sdata_experiments
rm dist/*.tar.gz
python setup.py sdist
#export TWINE_USERNAME=''
#export TWINE_PASSWORD=''
twine upload dist/*

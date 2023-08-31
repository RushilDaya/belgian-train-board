#!/bin/sh
mkdir -p package
rm -rf package
rm -rf build
rm -rf aq.egg-info
rm package.zip
mkdir -p package
pip install --force-reinstall --target ./package .
cd package 
zip -r ../package.zip .
cd ..
zip package.zip lambda_function.py
aws --profile personal --region eu-west-1 lambda update-function-code \
    --function-name  update-train-board \
    --zip-file fileb://package.zip
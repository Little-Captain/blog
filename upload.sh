#!/usr/bin/env bash

make html

blog=Little-Captain.github.io
cd $blog
git add .
git commit -m 'update blog'
git push origin master
cd -

git add .
git commit -m 'update blog'
git push origin master
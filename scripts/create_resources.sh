#!/bin/bash

working_dir='/Users/ssegurav/Source/github.com/thelastrkoch/capitalFocus.api/src/resources'
cd $working_dir

echo 'Please type the name of the new resource'
read resource_name

mkdir $resource_name
cd $resource_name
file_list=('controller.py' 'repository.py' 'service.py')
for file in ${file_list[@]}; do touch $file; done;
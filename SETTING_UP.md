# Intro
This document describes how to log in, run the apptainer container, cuda setup, container and how to start up jupyter (and 'tunnel' to it) if you so desire

## ssh setup and container

Please note that there is ```fail2ban``` running on our servers - which blocks offending ip after three incrrect password attemts - evn if the string provided is empty (i.e. 'Enter' was hit). Please ```CTRL+C``` if you are being asked for a password.
A configuration ssh file has been provided for you [here](https://github.com/wfedorko/TRISEP_2025_ssh_config) and some tips provided in the README there. Keep in mind that the location of the keys ```IdentityFile ~/.ssh/id_ed25519``` is assumed to be the default one. If you provided an alternatve location - you should change the value of these fields for both connections. 
You should have two connections named ```ML-TRISEP-CONTAINER``` and ```ML-TRISEP```. The first one will launch the apptainer container. The second one is a 'bare' login. Simply type ```ssh ML-TRISEP``` or ```ssh ML-TRISEP-CONTAINER``` on your laptop terminal.

If you want to use ```screen``` or ```tmux``` or ```nohup``` to run longer jobs while allowing for a network disconnect you can launch the container inside ```tmux/screen``` by copying and pasting the command specified by ```RemoteCommand``` fields specified in the ```ML-TRISEP-CONTAINER``` connection. 

## cuda setup and environment variable

Each group has been assigned a single GPU to share. This is specified by ```CUDA_VISIBLE_DEVICES``` environment variable which has been set on login (in your ```.bashrc``` file). Please do not change this. The GPUs can accept multiple concurrent jobs - but overloading GPU memory is likely to cause jobs crashing. Please discuss with your team mates as to who is running jobs on 'your' GPU at any given time and if it is ok to add anoter job.

## jupyter - starting up and connecting to

## github






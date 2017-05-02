#!/bin/bash

#Get architecture
ARCH=`uname -m`
if [ "$ARCH" == "armv6l" ] ; then
    DIR=""
elif [ "$ARCH" == "x86" ] ; then
    DIR="x86/"
elif [ "$ARCH" == "x86_64" ] ; then
    DIR="x64/"
fi
function python_dependencies() {
	echo "#####      Installing python modules      ############################"
	echo "-----      Installing SpeechRecognition   ----------------------------"
	#if [ $(pip freeze | grep SpeechRecognition )
	pip install SpeechRecognition
	echo "-----      Installing gTTS                ----------------------------"
	pip install gTTS
	echo "-----      Installing scikit              ----------------------------"
	pip install numpy
	pip install scipy
	pip install -U scikit-learn
	
}

function shell_dependencies() {
	if [ $(dpkg-query -W -f='${Status}' sox 2>/dev/null | grep -c "ok installed") -eq 0 ];
	then
		echo "-----      Installing Sox   ------------------------------------------"
		sudo apt-get install sox
	else
		echo "-----      sox already installed - skipping   ------------------------"
	fi
}

echo "---------------------------------"
echo "Installing dependencies for RAHMS"
echo "---------------------------------"

echo "Would you like to run the full install of RAHMS (y/n)"
read option
if [ $option == "y" ] || [ $option == "Y" ] ; 
	then
	python_dependencies;
	shell_dependencies;
else
	echo "Install python dependencies? These are needed for many of RAHMS applications!"
	read option
	if [ $option == "y" ] || [ $option == "Y" ] ; then
		python_dependencies
	fi
	echo "Install shell dependencies?"
	read option
	if [ $option == "y" ] || [ $option == "Y" ] ; then
		shell_dependencies
	fi
fi


function python_dependencies() {
	echo "#####      Installing python modules      ############################"
	echo "-----      Installing SpeechRecognition   ----------------------------"
	pip install SpeechRecognition
	echo "-----      Installing gTTS                ----------------------------"
	pip install gTTS
	
}

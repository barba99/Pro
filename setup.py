#!/bin/bash
clear
echo
echo "Wait Until The Process Is Complete.!"
echo
pip2 install mechanize 
clear
pip2 install requests 
echo
count=$((0))
anim=$((0))
while [[ $count -lt $((100)) ]]; do
    count=$((count+1))
    anim=$((anim+1))
    flag=$((count%2))
    if [[ $flag -eq $((0)) ]]; then
        bar="${bar}\e[92m█"
    fi

    if [[ $anim -eq $((1)) ]]; then
        step="\e[93m|"
    elif [[ $anim -eq $((3)) ]]; then
        step="\e[92m/"
    elif [[ $anim -eq $((9)) ]]; then
        step="\e[93m-"
    elif [[ $anim -eq $((12)) ]]; then
        step="\e[92m\\"
        anim=$((0))
    fi

    echo -ne "${step}${count}%[${bar}]\r"
    sleep 0.02
done
echo -ne "${count}%[${bar}]!!!\n"
sleep 2
clear
echo
# 1. Create ProgressBar function
# 1.1 Input is currentState($1) and totalState($2)
function ProgressBar {
# Process data
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done
# Build progressbar string lengths
    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

# 1.2 Build progressbar strings and print the ProgressBar line
# 1.2.1 Output example:                           
# 1.2.1.1 Progress : [########################################] 100%
printf "\e[92m\rProgress :\e[93m [${_fill// /#}${_empty// /-}] ${_progress}%%"

}

# Variables
_start=1

# This accounts as the "totalState" variable for the ProgressBar function
_end=100

# Proof of concept
for number in $(seq ${_start} ${_end})
do
    sleep 0.1
    ProgressBar ${number} ${_end}
done
printf '\nFinished!\n'
clear
echo
clear
sleep 20 & PID=$! #simulate a long process
clear
echo
python2 Pro

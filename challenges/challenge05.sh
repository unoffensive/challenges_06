#!/bin/bash

# Define the animation frames
frames=("|" "/" "-" "\\")

# Number of frames
num_frames=${#frames[@]}

# Duration to run the animation (in seconds)
duration=3

# Calculate the end time
end_time=$((SECONDS + duration))

# Clear the line
clear_line="\r\033[K"

echo "Loading..."

# Loop until the time is up
while [ $SECONDS -lt $end_time ]; do
    for ((i=0; i<num_frames; i++)); do
        # Print the frame
        echo -ne "${frames[i]}"
        
        # Delay for a short time (0.1 seconds)
        sleep 0.1
        
        # Clear the line and move back to the start
        echo -ne "$clear_line"
    done
done

echo "Your Description Loading Please Wait..."

frames=("|" "/" "-" "\\")
num_frames=${#frames[@]}
duration=3
end_time=$((SECONDS + duration))
clear_line="\r\033[K"

# Loop until the time is up
while [ $SECONDS -lt $end_time ]; do
    for ((i=0; i<num_frames; i++)); do
        # Print the frame
        echo -ne "${frames[i]}"
        
        # Delay for a short time (0.1 seconds)
        sleep 0.1
        
        # Clear the line and move back to the start
        echo -ne "$clear_line"
    done
done

echo "Zed it's a New Generation! You Have a *z_power* Directory within binary files, your mission is start a *workstyle* binary file firstly, after seconds you must press *CTRL+Z* in this time You Give A Life For Linux Processes It's Good but We may KILL all of them if we want, and be Patient in *endoflife* about 1 minute after KILLING!!!"

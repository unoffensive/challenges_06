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

echo "Do You Know about *happy_puzzle* I Just Love it, let's take a rest."

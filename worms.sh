# Flags
part1="RmxBZwo=="
part2="e3VfdmVfZm8K=="
part3="dW5kZWQK=="
part4="X3RoZV9mCg=="
part5="bEFnfQo=="

# Hidden files
mkdir -p /tmp/.hidden
echo $part1 > /tmp/.hidden/.part1.txt
echo $part2 > /tmp/.hidden/.part2.txt
echo $part3 > /tmp/.hidden/.part3.txt
echo $part4 > /tmp/.hidden/.part4.txt
echo $part5 > /tmp/.hidden/.part5.txt

# Creating Logs Files
echo "Log entry 1: $(date)" > /tmp/ctf_log1.log
echo "Log entry 2: $(date)" > /tmp/ctf_log2.log
echo "Log entry 3: $(date)" > /tmp/ctf_log3.log

# Creating Log Files
echo "Important data: $part1" >> /tmp/ctf_log1.log
echo "Important data: $part2" >> /tmp/ctf_log2.log
echo "Important data: $part3" >> /tmp/ctf_log3.log

echo "Logs and hidden files have been generated."

# Add options to ls command; shorten size with -l option & enable colorized output 
alias ls='ls -hG'
# Add user bin directory to the PATH variable
export PATH=~/bin:$PATH
# Change the prompt behaviour
export PS1='\[\e]0;\w\a\n\[\e[32m\]\u@\h \[\e[33m\]\w\[\e[0m\]\n\$ '
# Ensure that bash sort program behaves correctly
export LC_ALL=C
# Silence the message about changing the user shell script back to zsh
export BASH_SILENCE_DEPRECATION_WARNING=1

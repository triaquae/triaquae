SSH_COMPLETE=( $(cat ~/.ssh/known_hosts | \
cut -f 1 -d " " | \sed -e s/,.*//g | \
uniq ) )complete -o default -W "${SSH_COMPLETE[*]}" ssh

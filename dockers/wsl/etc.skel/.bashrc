# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# history settings
HISTCONTROL=ignoreboth # don't duplicate rows
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend # don't override history file

# check the window size after each command and, if necessary, update the values of LINES and COLUMNS
shopt -s checkwinsize

# make less more friendly for non-text input files
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set prompt
if [[ $EUID -ne 0 ]]; then
   PS1='\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;32m\]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
   PS1='\[\033[01;31m\]\u\[\033[00m\]:\[\033[01;32m\]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
fi


alias ls='ls --color=auto'
alias dir='dir --color=auto'
alias vdir='vdir --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias cmd='cmd.exe'
alias pws='powershell.exe'
alias pwsi='powershell_ise.exe'
alias home='cd /mnt/c/Users'
alias open='explorer.exe .'

# enable programmable completion features
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
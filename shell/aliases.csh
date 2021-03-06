alias ec 'emacsclient'
alias lsc 'ls --color=auto'  
alias lrtc 'ls --color=auto -lrt' 
alias lrt 'ls -lrt'
alias u "cd ../"
alias c "clear"
alias lf 'find $cwd/ -maxdepth 1'
alias la "ls -lha"
alias edu "ss edu/trn.jspatrick"
alias l "ls -lrt --color=auto"
alias egi "egrep -i"
alias gi "grep -i"
alias vlu 'vfolookup -shot $SHOT -show $SHOW '
alias diffPref "svn diff --diff-cmd meld -r PREV:HEAD" 
alias rdiff "svn diff --diff-cmd meld -r " 
alias rmSvnDirs "find . -type d -iname '.svn' | xargs -0 rm -rf"
alias md "svn diff --diff-cmd meld -r"
alias fnd 'find -L $PWD \( ! -type d -name ".*" -prune \) -o -iname '
alias mya 'maya --appver 2013-3.2SPI-mr'


#SPI aliases
alias maya 'maya -appver 2013-3.0SPI'
alias mel 'cd /shots/$SHOW/home/maya2013_prod/scripts/tools'
alias melD 'cd /shots/$SHOW/home/dev/jspatrick/maya2013_prod/scripts/tools'
alias pyD 'cd /shots/$SHOW/home/dev/jspatrick/maya2013_prod/python/common'
alias py 'cd /shots/$SHOW/home/maya2013_prod/python/common'
alias pyCom 'cd /shots/$SHOW/home/python/common'
alias pyComD 'cd /shots/$SHOW/home/dev/jspatrick/python/common'

alias voe 'vcco --empty'


alias devPP 'setenv PYTHONPATH /shots/${SHOW}/home/dev/${USER}/python/common:/shots/spi/home/dev/${USER}/python/common:${PYTHONPATH}'

alias sr "seqls -R"
alias wipe 'seqls -R |tail -n 2 |xargs | awk '\''{print "itview -lm " $1" -w "$2}'\'' | sh -v'

alias hvInfo 'vp-version-info -s $SHOW -st $SHOT -v highest -p '
alias cvInfo 'vp-version-info -s $SHOW -st $SHOT -v current -p '
alias avInfo 'vp-version-info -s $SHOW -st $SHOT -v approved -p '

alias spMel "cd /shots/spi/home/maya2013_prod/scripts/tools"
alias spMelD "cd /shots/spi/home/dev/jspatrick/maya2013_prod/mel/tools"
alias spPyD "cd /shots/spi/home/dev/jspatrick/maya2013_prod/python/common"
alias spPy "cd /shots/spi/home/maya2013_prod/python/common"
alias spPyCom "cd /shots/spi/home/python/common"
alias spPyComD "cd /shots/spi/home/dev/jspatrick/python/common"

alias spJ "source $HOME/spi_jump.csh;"

alias vcci_force "/shots/spi/home/bin/common/vcci"
alias vcci "/shots/cl2/home/bin/common/vcci_shy"

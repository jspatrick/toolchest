#Set a python path for custom shizz
set homePyPath = "$HOME/python"

if $?PYTHONPATH then
   if ($PYTHONPATH !~ *$homePyPath*) then
        echo "Appending "$homePyPath" to PYTHONPATH"
        setenv PYTHONPATH $PYTHONPATH":"$homePyPath
   else
        echo "Skipping setting PYTHONPATH - it's already set"
   endif
else
   echo "SETTING PYTHONPATH to "$homePyPath   
   setenv PYTHONPATH $homePyPath
endif


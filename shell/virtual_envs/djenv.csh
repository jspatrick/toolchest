setenv PROJECT_NAME "reality-pickem"
setenv PYTHON_APP_NAME "reality_pickem"
setenv PROJECT_ROOT "$HOME/dev/sites/djangoenv/$PYTHON_APP_NAME"
setenv DATABASE_URL "sqlite:///$PROJECT_ROOT/db.sqlite3"
setenv DJ_DEBUG "1"
source $HOME/dev/sites/djangoenv/bin/activate.csh
cd $PROJECT_ROOT



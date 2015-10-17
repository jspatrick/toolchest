# Makefile - for the custom package.
#
# Version: 1.9962

EMACS	= emacs
FLAGS	= -batch -q -no-site-file

WIDGET	= widget.el wid-edit.el widget-example.el wid-browse.el
CUSTOM	= custom.el cus-edit.el cus-face.el
SOURCE	= $(CUSTOM) $(WIDGET) 
TEXT	= Makefile widget.texi custom.texi ChangeLog TODO lpath.el \
	radio0.xpm radio1.xpm check0.xpm check1.xpm x-overlay.el \
	right.xpm down.xpm right-pushed.xpm down-pushed.xpm folder.xpm \
	face.xpm option.xpm


FSFSOURCE = $(CUSTOM) widget.el wid-edit.el wid-browse.el
DISTDIR = $(HOME)/.public_html/custom
FTPDIR  = $(HOME)/.public_ftp/custom

REMOVE = cus-start.el #none

.SUFFIXES: .el .elc .texi 

all:
	rm -f *.elc
	$(EMACS) $(FLAGS) -l ./lpath.el -f batch-byte-compile $(SOURCE)

some:	$(SOURCE:.el=.elc)

.el.elc:
	$(EMACS) $(FLAGS) -l ./lpath.el -f batch-byte-compile $<

dist:
	@if [ "X$(TAG)" = "X" ]; then echo "*** No tag ***"; exit 1; fi
	@if [ "X$(OLD)" = "X" ]; then echo "*** No old ***"; exit 1; fi
	perl -pi.bak -e "s/Version: $(OLD)/Version: $(TAG)/" \
		$(SOURCE) $(TEXT)
	perl -pi.bak -e "s/$(OLD)/$(TAG)/" $(DISTDIR)/index.html
	mv ChangeLog ChangeLog.old
	echo `date "+%Y-%m-%d "` \
	     " Per Abrahamsen  <abraham@dina.kvl.dk>" > ChangeLog
	echo >> ChangeLog
	echo "	* Version" $(TAG) released. >> ChangeLog
	echo >> ChangeLog
	cat ChangeLog.old >> ChangeLog
	if [ -d widget-$(TAG) ]; then rm -fr widget-$(TAG) ; fi
	rm -f $(REMOVE) 
	-cvs remove $(REMOVE) 
	-cvs add $(SOURCE) $(TEXT)
	cvs commit -m "Release $(TAG)"
	cvs tag release_`echo $(TAG) | sed -e 's/[.]/_/g'`
	mkdir custom-$(TAG) 
	cp $(SOURCE) $(TEXT) custom-$(TAG)
	tar -cf - custom-$(TAG) | gzip --best > $(FTPDIR)/custom-$(TAG).tar.gz
	cp widget-example.el $(DISTDIR)
	texi2html widget.texi
	makeinfo widget.texi
	texi2html custom.texi
	makeinfo custom.texi
	mv *.html $(DISTDIR)

fsf:
	( cd /gd/gnu/emacs/19.0/list; co $(FSFSOURCE) )

TAGS:
	etags $(SOURCE)

wc:
	wc $(SOURCE)

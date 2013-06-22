## setup symlinks, etc
EMACS_LINK = $(HOME)/.emacs.d

.PHONY: symlinks

all: emacs

symlinks: $(EMACS_LINK)

$(EMACS_LINK):
	ln -s $(EMACS_LINK) emacs


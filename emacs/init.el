;;;;;;;;;John Patrick's emacs config file;;;;;;;;;;
;; This initailization is split into several phases.

;; The config loads and configures various modes and settings.
;; The tools phase loads my custom global functions
;; The keybindings phase loads all custom keybindings

;; Finally, I have different tools and settings depending upon where I'm working.
;; I use jp_system_SYSTEMNAME.el files for system-specific/site-specifc setup.

; add ~/.emacs.d directory to load-path
(add-to-list 'load-path "~/.emacs.d/lisp/") ;;should be automatic

;; The root toolchest directory
(defvar toolchest-directory "~/toolchest")


(load "jp_config")
(load "jp_tools")
(load "jp_keybindings")

;--------------------LOAD SYSYTEM-SPECIFIC CONFIG--------------------

;; Get the name of our current system.
(defvar my-system-name 
  (cond (	 
	 ((memq system-type '(darwin)) "home") ;;Are we in OSX?
	 ))
;; Throw an error if we can't ID the current system
(if (eq my-system-name nil)
	(throw "no system" "Cannot identify the current system")
)

  
;; Find the load file and load it
(let ((system-load-file (concat "jp_system_" my-system-name )))
  (if (locate-file system-load-file load-path load-suffixes)	  
	  (progn
		(message (concat "loading: " system-load-file))
		(load system-load-file)
		)

	)
)

(put 'dired-find-alternate-file 'disabled nil)

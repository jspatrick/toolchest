;;;;;;;;;John Patrick's emacs config file;;;;;;;;;;
;; This initailization is split into several phases.

;; The config loads and configures various modes and settings.
;; The tools phase loads my custom global functions
;; The keybindings phase loads all custom keybindings

;; Finally, I have different tools and settings depending upon where I'm working.
;; I use jp_system_SYSTEMNAME.el files for system-specific/site-specifc setup.

; add ~/.emacs.d directory to load-path
(add-to-list 'load-path "~/.emacs.d")

;; The root toolchest directory
(defvar toolchest-directory "~/toolchest")


(load "jp_config")
(load "jp_tools")
(load "jp_keybindings")

;--------------------LOAD SYSYTEM-SPECIFIC CONFIG--------------------

;; Get the name of our current system.
(defvar my-system-name 
  (cond ((memq system-type '(gnu/linux)) "spi")
		;;Are we in OSSX
		((memq system-type '(darwin)) "home")
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


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(safe-local-variable-values (quote ((python-shell-interpreter-args . "/Users/john/Sites/reality-pickem/manage.py shell") (python-shell-interpreter . "python")))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

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
(load "jp_system_home")


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("0d3fb10835e185b4b350b1bd902ca452e795b9e9fc7f6e8a5eebb9d146f9beff" default)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

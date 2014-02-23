;;;;;;;;;John Patrick's emacs config file;;;;;;;;;;

; add ~/.emacs.d directory to load-path
(add-to-list 'load-path "~/.emacs.d")
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes")

;;--------------------global settings--------------------
;; Am i at work?  some things will need to be configured differently if so
(defvar am-i-at-work 
  (eq system-type 'gnu/linux)
  "am I at work?")

(defvar maya-python-interpreter 
  (expand-file-name "~/virtual_mayapy/bin/python")
  "The python interpreter to use when using flymake, jedi, etc on 
   a maya file")

(defvar standard-python-interpreter
  (expand-file-name "~/virtual_mayapy/bin/python")
  "The python interpreter to use when using flymake, jedi, etc on 
   a standard file")

(defvar maya-pylint-cmd
  (concat (file-name-directory maya-python-interpreter)
          "epylint")
  "The pylint binary to use"
)

;;Marmalade package mgr
(require 'package)
(add-to-list 'package-archives
  '("melpa" . "http://melpa.milkbox.net/packages/") t)
(package-initialize)

;;colors
;(load-theme 'solarized-dark t)
(load-theme 'monokai t)

;OSX key mods
(setq mac-option-key-is-meta nil)
(setq mac-command-key-is-meta t)
(setq mac-command-modifier 'meta)
(setq mac-option-modifier nil)

;;turn off the alarm bell
(setq visible-bell 1)
(set-keyboard-coding-system nil)

;;dired setup
(put 'dired-find-alternate-file 'disabled nil)

;; shell setup
(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)

;; inserting at a point
(delete-selection-mode t)

;; highlight during searching
(setq query-replace-highlight t)

;; highlight incremental search
(setq search-highlight t)

;; Automatically reload files after they've been modified
(global-auto-revert-mode 1)
(put 'upcase-region 'disabled nil)


; fix clipboard issues
(set-clipboard-coding-system (quote x-ctext-unix))
(setq x-select-enable-clipboard t)

;; Supress the GNU startup message
(setq inhibit-startup-message t)

;; setup an emacs server

;; (defvar server-buffer-clients)
;; (when (and (fboundp 'server-start) (string-equal (getenv "TERM") 'xterm))
;;   (server-start)
;;   (defun fp-kill-server-with-buffer-routine ()
;;     (and server-buffer-clients (server-done)))
;;   (add-hook 'kill-buffer-hook 'fp-kill-server-with-buffer-routine))

;don't autosave or make backups
(setq make-backup-files nil) ; stop creating those backup~ files
(setq auto-save-default nil) ; stop creating those #auto-save# files

;; No tabs-- use spaces when indenting (doesn't affect Makefiles,
;; does affect text files and code, doesn't affect existing tabs).
;; The use of setq-default means this only affects modes that don't
;; overwrite this setting.
(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)

;; turn off scroll bar and tool bar
(if (fboundp 'scroll-bar-mode) (scroll-bar-mode -1))
(if (fboundp 'tool-bar-mode) (tool-bar-mode -1))

; Line numbers
(require `linum)
(global-linum-mode 1)



;;--------------------XML--------------------
(defun nxml-mode-additional-keys ()
    "Key bindings to add to `nxml-mode'."
    (require 'sgml-mode)
    (define-key nxml-mode-map (kbd "M-/") 'nxml-complete)
    (define-key nxml-mode-map (kbd "\t") 'sgml-indent-line)
    )

(add-hook
 'nxml-mode-hook
 'nxml-mode-additional-keys
)

(require 'sgml-mode)
(setq auto-mode-alist
      (append '(("\\.xml" . sgml-mode))
              auto-mode-alist))


;;--------------------MAIL---------------------
(setq mail-user-agent 'message-user-agent)
(setq user-full-name "John Patrick")

(if am-i-at-work
    (setq user-mail-address "jspatrick@imageworks.com")
  (setq user-mail-address "jspatrick@gmail.com"))
  

;;--------------------ORG-----------------------
(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(add-hook 'org-mode-hook 'turn-on-font-lock)
(global-set-key "\C-cl" 'org-store-link)
(global-set-key "\C-ca" 'org-agenda)
(global-set-key "\C-cb" 'org-iswitchb)
(setq org-agenda-files (list "~/todo.org"))



;;--------------------EPC--------------------
(require 'epc)

;;--------------------C++--------------------
(setq-default c-basic-offset 4 c-default-style "linux")
(setq-default tab-width 4 indent-tabs-mode t)
(setq-default c-default-style)

(require 'auto-complete-clang)
(defun my-ac-cc-mode-setup ()
  (setq ac-sources (append '(ac-source-clang) ac-sources)))
(add-hook 'c-mode-common-hook 'my-ac-cc-mode-setup)


;;--------------------PYTHON--------------------
(require 'python)
(autoload 'jedi:setup "jedi" nil t)
(setq jedi:setup-keys t)
(setq jedi:complete-on-dot t)
(add-hook 'python-mode-hook (lambda () 
                              (jedi:setup)
                              (if am-i-at-work
                                  (setq jedi:server-command
                                        (list maya-python-interpreter 
                                              (expand-file-name "elpa/jedi-20130714.1415/jediepcserver.py"))
                                        )
								;; (setq jedi:server-command
                                ;;         (list "python" 
                                ;;               (expand-file-name "~/.emacs.d/elpa/jedi-20130714.1415/jediepcserver.py"))
                                ;;         )
                                )
                              ))
;;django mode
(require 'python-django)


;;flymake error checking
(when (load "flymake" t)
  (defun flymake-pylint-init ()
     (let* ((temp-file (flymake-init-create-temp-buffer-copy
                        'flymake-create-temp-inplace))
            (local-file (file-relative-name
                         temp-file
                         (file-name-directory buffer-file-name))))
       
           (list maya-pylint-cmd
                 (list local-file))))

       (add-to-list 'flymake-allowed-file-name-masks
                '("\\.py\\'" flymake-pylint-init)))

;; To avoid having to mouse hover for the error message, these functions make flymake error messages
;; appear in the minibuffer
(defun show-fly-err-at-point ()
  "If the cursor is sitting on a flymake error, display the message in the minibuffer"
  (require 'cl)
  (interactive)
  (let ((line-no (line-number-at-pos)))
    (dolist (elem flymake-err-info)
      (if (eq (car elem) line-no)
      (let ((err (car (second elem))))
        (message "%s" (flymake-ler-text err)))))))


(add-hook 'post-command-hook 'show-fly-err-at-point)


;--------------------AUTO COMPLETE--------------------
(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d//ac-dict")
(ac-config-default)
(setq ac-use-fuzzy nil)
(setq ac-delay 0.1)
(setq ac-quick-help-delay 1.0)
(setq ac-show-menu-immediately-on-auto-complete t)
(global-auto-complete-mode t)



;--------------------Other--------------------
;yaml mode
(require 'yaml-mode)
(add-to-list 'auto-mode-alist '("\\.yml$" . yaml-mode))
(add-to-list 'auto-mode-alist '("\\.yaml$" . yaml-mode))

;buffer extension
(require 'buffer-extension)
(global-set-key (kbd "<f8>") 'copy-buffer-file-name-as-kill)

;; get C and C++ editting to work on the proper files
(setq auto-mode-alist
      (append '(("\\.c$" . c-mode)
                ("\\.h$" . c++-mode)
                ("\\.C$" . c++-mode)
                ("\\.cpp$" . c++-mode)
                ("\\.tcc$" . c++-mode)
                ("\\.mel$"  . c++-mode)
                ("\\.c[+][+]$" . c++-mode))
              auto-mode-alist))


    
(defun jp-todo ()
 "Open my todo list"
 (interactive)
 (find-file "/net/homedirs/jspatrick/todo.org")
 (outline-mode))

(defun jp-notes ()
 "Open my todo list"
 (interactive)
 (find-file "/net/homedirs/jspatrick/notes.org")
 (outline-mode))

(defun jp-new-frame()
 "Create new frame"
 (interactive)
 (make-frame-command)
 (load-file "~/.emacs.d/init.el"))

(defun jp-insert-setAttr ()
 "insert setattr command"
 (interactive)
 (insert "MC.setAttr(\"%s."))


(defun kill-all-dired-buffers()
  "Kill all dired buffers."
  (interactive)
  (save-excursion
    (let((count 0))
      (dolist(buffer (buffer-list))
        (set-buffer buffer)
        (when (equal major-mode 'dired-mode)
          (setq count (1+ count))
          (kill-buffer buffer)))
      (message "Killed %i dired buffer(s)." count ))))




;; someday might want to rotate windows if more than 2 of them
(defun swap-windows ()
  "If you have 2 windows, it swaps them."
  (interactive) (cond ((not (= (count-windows) 2)) (message "You need exactly 2 windows to do this."))
                      (t
                       (let* ((w1 (first (window-list)))
                              (w2 (second (window-list)))
                              (b1 (window-buffer w1))
                              (b2 (window-buffer w2))
                              (s1 (window-start w1))
                              (s2 (window-start w2)))
                         (set-window-buffer w1 b2)
                         (set-window-buffer w2 b1)
                         (set-window-start w1 s2)
                         (set-window-start w2 s1)))))

(defun rename-file-and-buffer (new-name)
"Renames both current buffer and file it's visiting to NEW-NAME."
(interactive "sNew name: ")
(let ((name (buffer-name))
      (filename (buffer-file-name)))
(if (not filename)
      (message "Buffer '%s' is not visiting a file!" name)
(if (get-buffer new-name)
       (message "A buffer named '%s' already exists!" new-name)
      (progn
    (rename-file name new-name 1)
    (rename-buffer new-name)
    (set-visited-file-name new-name)
    (set-buffer-modified-p nil))))))


(defun move-buffer-file (dir)
  "Moves both current buffer and file it's visiting to DIR."
  (interactive "DNew directory: ")
  (let* ((name (buffer-name))
         (filename (buffer-file-name))
         (dir
          (if (string-match dir "\\(?:/\\|\\\\)$")
              (substring dir 0 -1) dir))
         (newname (concat dir "/" name)))

    (if (not filename)
        (message "Buffer '%s' is not visiting a file!" name)
      (progn
        (copy-file filename newname 1)
        (delete-file filename)
        (set-visited-file-name newname)
        (set-buffer-modified-p nil)  t))))


(require 'misc)
;--------------------KEY BINDINGS--------------------
(ffap-bindings)
(global-set-key (kbd "C-c f") 'ffap-other-window)
(global-set-key (kbd "M-a") 'jp-insert-setAttr)
(global-set-key (kbd "C-<tab>") 'ac-start)

(global-set-key (kbd "C-c 3") 'comment-region)
(global-set-key (kbd "C-c #") 'uncomment-region)

(setq bs-cycle-configuration-name "files")
(global-set-key (kbd "M-C-<") 'bs-cycle-next)
(global-set-key (kbd "M-C->") 'bs-cycle-previous)
;; todo: customize the cycle configuration to visit shell, python, etc

(global-set-key (kbd "C-z") 'undo)
(global-set-key (kbd "M-s") 'replace-string)
(global-set-key (kbd "M-r") 'replace-regexp)
(global-set-key (kbd "C-x M-r") 'search-forward-regexp)
(global-set-key (kbd "M-B") 'rename-buffer)
(global-set-key (kbd "C-x j") 'python-django-open-project)

;--------------------SITE SPECIFIC--------------------
;; load imageworks stuff if at imageworks
(if am-i-at-work
    (load "imageworks"))
(load "my_tools")
; run in server mode, so new requests can use 'emacsclient' to visit files in current session
;;(server-start)


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(send-mail-function (quote smtpmail-send-it))
 '(smtpmail-smtp-server "localhost")
 '(smtpmail-smtp-service 25))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )


;;;;;;;;;John Patrick's emacs config file;;;;;;;;;;
; add ~/.emacs.d directory to load-path
(add-to-list 'load-path "~/.emacs.d")
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes")

;; Am i at work?  some things will need to be configured differently if so
(defvar am-i-at-work (eq system-type 'gnu/linux) "am I at work?")

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


;;--------------------PYTHON--------------------
(autoload 'jedi:setup "jedi" nil t)
(setq jedi:setup-keys t)
(setq jedi:complete-on-dot t)
(add-hook 'python-mode-hook 'jedi:setup)
;(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))
;(require 'python-mode)

;;rope for autocompletion and refactoring
;; (require 'pymacs)
;; (autoload 'pymacs-apply "pymacs")
;; (autoload 'pymacs-call "pymacs")
;; (autoload 'pymacs-eval "pymacs" nil t)
;; (autoload 'pymacs-exec "pymacs" nil t)
;; (autoload 'pymacs-load "pymacs" nil t)

;; (pymacs-load "ropemacs" "rope-")
;; (pymacs-exec  "import rope.base.project;rope.base.project.Project('/shots/cl2/home/dev/jspatrick/maya2013_prod/python/common/')")
;; (rope-open-project "/shots/cl2/home/dev/jspatrick/maya2013_prod/python/common/")

;; (setq ropemacs-enable-autoimport t)
;; ;rope shortcuts
;; (define-key ropemacs-local-keymap "\M-?" 'rope-code-assist)


;;flymake error checking
(when (load "flymake" t)
  (defun flymake-pylint-init ()
     (let* ((temp-file (flymake-init-create-temp-buffer-copy
                        'flymake-create-temp-inplace))
            (local-file (file-relative-name
                         temp-file
                         (file-name-directory buffer-file-name))))
           (list "epylint" (list local-file))))

       (add-to-list 'flymake-allowed-file-name-masks
                '("\\.py\\'" flymake-pylint-init)))

;;display flymake errors in minibuffer
(require 'flymake-cursor)

; this get called after python mode is enabled
(defun py-outline-level ()
  (let (buffer-invisibility-spec)
    (save-excursion
      (skip-chars-forward "    ")
      (current-column))))

(defun my-python-outline-hook ()
  ; outline uses this regexp to find headers. I match lines with no indent and indented "class"
  ; and "def" lines.
  ;(setq outline-regexp "[^ \t]\\|[ \t]*\\(def\\|class\\) ")
  (setq outline-regexp "[ \t]*\\(def\\|class\\|@\\) ")
  ; enable our level computation
  (setq outline-level 'py-outline-level)
  ; do not use their \C-c@ prefix, too hard to type. Note this overides some bindings.
  (setq outline-minor-mode-prefix "\C-t")
  ; turn on outline mode
  (outline-minor-mode t)
  ; initially hide all but the headers
  ;(hide-body)
  ; make paren matches visible
  (show-paren-mode 1)
)

;; code folding
(add-hook 'python-mode-hook 'my-python-outline-hook)
; this gets called by outline to deteremine the level. Just use the length of the whitespace


; Outline-minor-mode key map
 (define-prefix-command 'cm-map nil "Outline-")
 ; HIDE
 (define-key cm-map "q" 'hide-sublevels)    ; Hide everything but the top-level headings
 (define-key cm-map "t" 'hide-body)         ; Hide everything but headings (all body lines)
 (define-key cm-map "o" 'hide-other)        ; Hide other branches
 (define-key cm-map "c" 'hide-entry)        ; Hide this entry's body
 (define-key cm-map "l" 'hide-leaves)       ; Hide body lines in this entry and sub-entries
 (define-key cm-map "d" 'hide-subtree)      ; Hide everything in this entry and sub-entries
 ; SHOW
 (define-key cm-map "a" 'show-all)          ; Show (expand) everything
 (define-key cm-map "e" 'show-entry)        ; Show this heading's body
 (define-key cm-map "i" 'show-children)     ; Show this heading's immediate child sub-headings
 (define-key cm-map "k" 'show-branches)     ; Show all sub-headings under this heading
 (define-key cm-map "s" 'show-subtree)      ; Show (expand) everything in this heading & below
 ; MOVE
 (define-key cm-map "u" 'outline-up-heading)                ; Up
 (define-key cm-map "n" 'outline-next-visible-heading)      ; Next
 (define-key cm-map "p" 'outline-previous-visible-heading)  ; Previous
 (define-key cm-map "f" 'outline-forward-same-level)        ; Forward - same level
 (define-key cm-map "b" 'outline-backward-same-level)       ; Backward - same level
 (global-set-key "\M-o" cm-map)



(require 'auto-complete-config)
(add-to-list 'ac-dictionary-directories "~/.emacs.d//ac-dict")
(ac-config-default) 
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
                ("\\.mel$"  . mel-mode)
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

;; Set some keys
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

;--------------------SITE SPECIFIC--------------------
;; load imageworks stuff if at imageworks
(if am-i-at-work
    (load "imageworks"))

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

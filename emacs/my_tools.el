(defun get-python-bin ()
"Get the current python binary to use, based on the current virtualenv"
(interactive "")
(concat python-shell-exec-path python-shell-interpreter)
)


(defun ask-to-save-buffer ()
  "Ask to save this buffer"
   (if (buffer-modified-p)
        (if (yes-or-no-p (concat "Save file?: " (buffer-file-name)))
            (save-buffer)
          )
     ))


(defun python-compile (&optional args)
  "Run the current file"
  (interactive "sAdditional args: ")
  (let ((this-buffer-file (buffer-file-name))
        (compilation-ask-about-save nil)
        (compilation-save-buffers-predicate '(lambda () nil))
        (cmd nil))
    (setq cmd (concat (get-python-bin) " " (buffer-file-name)))
    (if args
        (setq cmd (concat cmd " " args))
      )
    
    ;;save this buffer if it's modified
    (ask-to-save-buffer)
    (message "Running [%s]" cmd)
    (compile cmd)
  )
)



(defun python-compile-dev-mode ()
  "Set dev mode"
  (interactive "")
  (setenv "PYTHONPATH" (concat "/shots/spi/home/dev/jspatrick/python/common:"
           (getenv "PYTHONPATH")
           ))
)

(defun python-compile-edu ()
  "Set dev mode"
  (interactive "")
  (setenv "SHOW" "edu")
  (setenv "SHOW" "dev.home")
)


(defvar python-test-cmd "pytest"
 "Command to use for python unit testing"
  )

(defun python-pytest (&optional args)
  (interactive "s unittest args: ")
  (let ((this-buffer-file (buffer-file-name))
        (compilation-ask-about-save nil)
        (compilation-save-buffers-predicate '(lambda () nil))
        (cmd nil)
        (file-name buffer-file-name)
        ;; (process-environment (cons 
        ;;                       (concat "PYTHONPATH="
        ;;                              (file-name-directory buffer-file-name) 
        ;;                              ":" 
        ;;                              (getenv "PYTHONPATH"))
        ;;                       process-environment))
        )
    
    (if (eq args "")
      (setq cmd (concat python-test-cmd " " args))
      (setq cmd (concat python-test-cmd " " file-name))
      )
    ;;save this buffer if it's modified
    (ask-to-save-buffer)

    (message "Running [%s]" cmd)
    (compile cmd)
  )
)


(global-set-key (kbd "C-c C-c") 'python-compile)
(global-set-key (kbd "C-c t") 'python-pytest)
(global-set-key (kbd "C-c t") 'python-pytest)
(global-set-key (kbd "C-c o") (lambda () "" (interactive "") (occur "^def\\|^class")))
(global-set-key (kbd "C-c C-o") (lambda () "" (interactive "") (kill-buffer "*Occur*")))


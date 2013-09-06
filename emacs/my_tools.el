(defvar python-bin "python"
"the python command to run when compiling")

(defun python-compile (&optional args)
  "Run the current file"
  (interactive "sAdditional args: ")
  (let ((this-buffer-file (buffer-file-name))
        (compilation-ask-about-save nil)
        (compilation-save-buffers-predicate '(lambda () nil))
        (cmd nil))
    (setq cmd (concat python-bin " " (buffer-file-name)))
    (if args
        (setq cmd (concat cmd " " args))
      )
    
    ;;save this buffer if it's modified
    (if (buffer-modified-p)
        (if (yes-or-no-p (concat "Save file?: " (buffer-file-name)))
            (save-buffer)
            ))

    (message "Running [%s]" cmd)
    (compile cmd)
  )
)
 
(global-set-key (kbd "C-c C-c") 'python-compile)

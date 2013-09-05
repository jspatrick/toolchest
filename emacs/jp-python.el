;;extra python utilities

(setq compilation-scroll-output t)
(defun jp-py-run ()
  "Use compile to run python programs"
  (interactive)
  (compile (concat "python " (buffer-name))))

;; when in python mode, use the scrolling output
(add-hook 'python-mode-hook
          (lambda () 
            (make-local-variable 'compilation-scroll-output)
            (setq compilation-scroll-output t)))





(message "loading jp's home setup")

(add-to-list 'load-path "~/lintnode")
(require 'flymake-jslint)
;; Make sure we can find the lintnode executable
(setq lintnode-location "~/lintnode")
;; JSLint can be... opinionated
(setq lintnode-jslint-excludes (list 'nomen 'undef 'plusplus 'onevar 'white))
;; Start the server when we first open a js file and start checking
(add-hook 'js-mode-hook
          (lambda ()
            (lintnode-hook)))


(defun jp-goto-reality-pickem ()
  "go to rp root"
  (interactive "")
  (dired "/Users/jp/dev/reality-pickem/reality-pickem-root/")
  )

(global-set-key (kbd "C-x r") 'jp-goto-reality-pickem)



;;; cue3.el --- 

;; Copyright 2010 John Hood
;;
;; Author: jhood@hawk294.spimageworks.com
;; Version: $Id: cue3.el,v 0.0 2010/05/12 16:56:28 jhood Exp $
;; Keywords: 
;; X-URL: not distributed yet

;; This program is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2, or (at your option)
;; any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program; if not, write to the Free Software
;; Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

;;; Commentary: 

;; 

;;; Todo: 
;;;   Add outputs - get from python module
;;;     job = Cue3.findJob('htr-rev190-knagy_lfxprep_qc_render_120301_101937')
;;;     for layer in job.getLayers():
;;;     layer.proxy.getOutputPaths()

;; Put this file into your load-path and the following into your ~/.emacs:
;;   (require 'cue3)

;;; Code:


;;;;##########################################################################
;;;;  User Options, Variables
;;;;##########################################################################


(defvar cue3-job-regex "^[+-]\\(Running\\|Failing\\|Paused\\)[ ]+\\[[\\*-]+\\][ ]+\\(.*\\)$")
(defvar cue3-frame-regex "^[+-][ ]+\\([0-9]+-[^ ]+\\)[ ]+\\(Succeeded\\|Depend\\|Running\\|Eaten\\|Dead\\|Waiting\\)[ ]+.*")
(defvar cue3-timer nil)
(defvar cue3-job-expand nil)
(defvar cue3-search-history ())
(defvar cue3-mode-syntax-table "Syntax table for cue3 mode")
(defvar cue3-mode-abbrev-table "Abbrev table")
(defvar cue3-mode-map nil "Keymap for cue3-mode")
(defvar cue3-command-script (expand-file-name "~/.emacs.d/cue3Lib.py"))
;(setq cue3-command-script "/net/homedirs/jhood/.emacs.d/lisp/cue3Lib.py")
(defvar cue3-watch-history ())
(defvar cue3-watch-active t)

(defvar cue3-old-jobs ())

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; New Stuff here
;;





;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; core procedures
;;


(defun cue3-install-timer ()
  (interactive)
  (setq cue3-timer 
        (run-at-time nil 61 'cue3-update-jobs-list)))

(defun cue3-uninstall-timer ()
  (interactive)
  (if cue3-timer
  (cancel-timer cue3-timer))
  (setq cue3-timer nil))

(defun cue3-is-string-in-list (item rest)
  (if rest
      (progn
        (if (string= item (car rest))
            t
          (cue3-is-string-in-list item (cdr rest))))))


(defmacro cue3-with-cue-buffer (&rest subexprs)
  `(let ((tbuf (get-buffer-create "cue_jobs")))
     (save-excursion
       (set-buffer tbuf)
       (let ((result (progn ,@subexprs)))
         result))))

(defun cue3-get-listed-jobs ()
  (interactive)
  (cue3-with-cue-buffer
   (beginning-of-buffer)
   (let ((pos (re-search-forward cue3-job-regex (point-max) t))
         (result ()))
     (while pos
       (setq result (cons (match-string 2) result))
       (setq pos (re-search-forward cue3-job-regex (point-max) t)))
     result)))

(defun cue3-list-jobs (&optional expr)
  (interactive)
  (unless expr
    (setq expr (read-from-minibuffer "Expr: " (car cue3-search-history) nil nil 'cue3-search-history nil)))
  ;(add-to-history 'cue3-search-history expr)
  (setq cue3-search-history (delete-dups cue3-search-history))
  ;(unless (cue3-is-string-in-list expr cue3-search-history)
      ;(setq cue3-search-history (cons expr cue3-search-history)))

  ;(switch-to-buffer-other-window (cue3-update-jobs-list)))
  (let ((buf (cue3-update-jobs-list)))
   (if (not (get-buffer-window-list buf))
       (switch-to-buffer-other-window buf))))
        

(defun cue3-get-job-outputs (job &optional layer)
  (interactive)
  (cond (layer
     (message "Layer: %s" layer)
     (car (split-string (shell-command-to-string (concat "python2.5 " cue3-command-script " -o -f " layer " " job)))))
   ((equal layer nil)
     (car (split-string (shell-command-to-string (concat "python2.5 " cue3-command-script " -o " job)))))))
    
(defun cue3-itview-job-outputs-at-point ()
  (interactive)
    (let ((frame (cue3-get-frame-at-point))
       (job (cue3-get-nearest-job)))
       (cond ((and job frame)
         (message "Attempting to launch itview for frame %s" (car (cdr frame)))
         (cue3-itview-job-outputs (car (cdr job)) (car (cdr frame)))
       ((message "Attempting to launch itview for job %s" % (car (cdr job)))
        (cue3-itview-job-outputs (car (cdr job))))))))

(defun cue3-itview-job-outputs-at-point ()
  (interactive)
  (message "Attempting to launch itview")
    (let ((frame (cue3-get-frame-at-point))
       (job (cue3-get-nearest-job)))
      (cond 
         ((and job frame)
           (cue3-itview-job-outputs (car (cdr job)) (car (cdr frame))))
         (job
           (cue3-itview-job-outputs (car (cdr job)))))))


(defun cue3-itview-job-outputs (job &optional frame)
  (interactive)
  (cond (job
         (let ((output (cue3-get-job-outputs job frame)))
           (message "itview %s" output)
           (cond (output
                  (call-process "itview" nil 0 nil output))
                 ((equal output nil)
                  (message "No ouputs for %s" job)))))))

(defun cue3-itview-job-outputs (job &optional frame)
  (interactive)
  (cond (job
         (let ((output (cue3-get-job-outputs job frame)))
           (message "itview %s" output)
           (cond (output
                  (call-process "itview" nil 0 nil output))
                 ((equal output nil)
                  (message "No ouputs for %s" job)))))))


(defun -set (a b)
  "return list of elements in a but not b"
  (let ((src a)
        (result ()))
    (while (car src)
      (message "Checking %s" (car src))
      (when (member-ignore-case (car src) b)            
        (setq result (cons (car src) result)))
      (setq src (cdr src))
      (message "  %s" (cdr src)))
    result))

(defun cue3-kill-buffer ()
  (cue3-uninstall-timer))

(defun cue3-update-jobs-list ()
  (interactive)
  (unless cue3-timer (cue3-install-timer))
  (let ((buf (get-buffer-create "cue_jobs")))
    (set-buffer buf)
    (cue3-mode)    
    (add-hook 'kill-buffer-hook 'cue3-kill-buffer t t)
    (let ((current (cue3-get-name-at-point))
          (term (car cue3-search-history)))

      (setq buffer-read-only nil)
      ;(setq cue3-old-jobs (cue3-get-listed-jobs))
      (erase-buffer)
      (insert (concat "Expr:   " term "      Time: " (format-time-string "%T") "\n"))
      
      (if (and cue3-watch-active (car cue3-watch-history))
          (insert (format "Watching: %s\n" (car cue3-watch-history))))

      (insert "\n")

      (if cue3-job-expand
          (insert (call-process "python2.5" nil t nil cue3-command-script "-l" "-e" cue3-job-expand term))
        (insert (call-process "python2.5" nil t nil cue3-command-script "-l" term)))
                                        ; remove last char
      (goto-char (point-max))
      (delete-backward-char 2)

      (insert "\n")

      ;; insert old jobs
      ;(let ((diff (-set (cue3-get-listed-jobs) cue3-old-jobs)))
      ;  (while (car diff) 
      ;    (insert (format "+Succeeded %s\n" (car diff)))
      ;    (setq diff (cdr diff))))
         


      (when cue3-job-expand	
	(goto-char (point-min))
	(let ((jobMatch (search-forward cue3-job-expand nil t)))
	  (when (not (eq nil jobMatch))
	    (goto-char jobMatch)
	    (insert "\n")
	    (call-process "python2.5" nil t nil cue3-command-script "--getComments" cue3-job-expand)
	    (delete-backward-char 2)
	    )))


      (when current
        (cue3-go-to-job-and-frame (car current) (car (cdr current))))
      
     (font-lock-fontify-buffer)
     (setq buffer-read-only t)
    buf)))
      
(defun cue3-test ()
  (interactive)
  (message "%s" (current-buffer)))

(defun cue3-set-watch-term (arg)
  (interactive (list (read-from-minibuffer "Watch: " (car cue3-watch-history) nil nil 'cue3-watch-history nil)))
  (setq cue3-watch-active t)
  (cue3-update-jobs-list))
           
(defun cue3-set-watch (&optional val)
  (interactive)
  (cond (val
         (setq cue3-watch-active t))
        (t
         (setq cue3-watch-active (not cue3-watch-active))))
  (cue3-update-jobs-list))
  
(defun cue3-expand-job-at-point ()
  (interactive)
  (let ((job (or (cue3-get-job-at-point) (cue3-get-nearest-job))))
    (when job
      (let ((jobName (car (cdr job))))
        (if (string= cue3-job-expand jobName)
            (setq cue3-job-expand nil)
          (setq cue3-job-expand jobName))
        (cue3-update-jobs-list)))))
        
(defun cue3-get-job-at-point ()
  "Return (status, jobname)"
  (interactive)
  (save-excursion
    (beginning-of-line)
    (when (looking-at cue3-job-regex)
      (let ((jobstr (substring (match-string 0) 1)))
	(let ((jobl (split-string jobstr)))
	  (let ((job (list (car jobl) (car (last jobl)))))	    
	    job))))))


(defun cue3-get-job-at-point-2 ()
  "Return (status, jobname)"
  (interactive)
  (save-excursion
    (beginning-of-line)
    (when (looking-at cue3-job-regex)
      (list (match-string-no-properties 1) (match-string-no-properties 2)))))


(defun cue3-get-nearest-job ()
  "Return (status, jobname)"
  (interactive)
  (save-excursion
    (cue3-get-job-at-point-impl)))

(defun cue3-get-nearest-job-2 ()
  "Return (status, jobname)"
  (interactive)
  (save-excursion
    (beginning-of-line)
    (while (and (not (looking-at cue3-job-regex)) (not (eq (point) (point-min))))
      (beginning-of-line 0))
    (if (looking-at cue3-job-regex)
      (list (match-string-no-properties 1) (match-string-no-properties 2)))))

(defun cue3-get-job-at-point-impl ()
  (beginning-of-line)
  
  (while (and (not (looking-at cue3-job-regex)) (not (eq (point) (point-min))))
    (beginning-of-line 0))
  (if (looking-at cue3-job-regex)
      (let ((jobstr (substring (match-string 0) 1)))
	(let ((jobl (split-string jobstr)))
	  (let ((job (list (car jobl) (car (last jobl)))))	    
	    job)))))

(defun cue3-comment-job-at-point ()
  (interactive)
  (let ((job (cue3-get-nearest-job)))
    (let( (subject (read-from-minibuffer (format "Comment subject for %s: " (car (cdr job)))))
	  (comment (read-from-minibuffer (format "Comment body for %s: " (car (cdr job))))) )
      (message (format "Adding comment [%s] to job %s" comment (car (cdr job))))
      (call-process "python2.5" nil t nil cue3-command-script "--subject" subject "--comment" comment (car (cdr job)))
      )
    )
  )


(defun cue3-email-artist ()
  (interactive)
  (let ((job (cue3-get-nearest-job)))
    (when (job)
      (print (format "Email owner of job %s" (car (cdr job)))))))

(defun cue3-get-frame-at-point ()
  (interactive)

  (save-excursion
    (beginning-of-line)
    (when (looking-at cue3-frame-regex)
      (list (match-string 2) (match-string 1)))))

(defun cue3-eat-frame-at-point ()
  (interactive)
  (let ((frame (cue3-get-frame-at-point))
        (job (cue3-get-nearest-job)))
    (when (and frame job (y-or-n-p (format "Eat frame %s " (car (cdr frame)))))
      (call-process "python2.5" nil t nil cue3-command-script "-x" "-f" (car (cdr frame)) (car (cdr job)))
       (cue3-update-jobs-list))))
      
(defun cue3-drop-depends-frame-at-point ()
  (interactive)
  (let ((frame (cue3-get-frame-at-point))
        (job (cue3-get-nearest-job)))
    (when (and frame job (y-or-n-p (format "Satisfy depends for %s " (car (cdr frame)))))
      (call-process "python2.5" nil t nil cue3-command-script "-d" "-f" (car (cdr frame)) (car (cdr job)))
      (cue3-update-jobs-list))))

(defun cue3-retry-all-dead-frames-at-point ()
  (interactive)
  (let ((job (cue3-get-nearest-job)))
    (when (and job (y-or-n-p (format "Retry all dead frames in job %s " (car (cdr job)))))
      (call-process "python2.5" nil t nil cue3-command-script "-r" "-a" (car (cdr job)))
      (cue3-update-jobs-list))))

(defun cue3-retry-or-resume-at-point ()
  (interactive)
  (let ((frame (cue3-get-frame-at-point))
       (job (cue3-get-nearest-job)))
    (cond
     ((and frame 
           (not (string= "Depend" (car frame)))
           (not (string= "Eaten" (car frame)))
           (y-or-n-p (format "Retry frame %s " (car (cdr frame)))))
      (call-process "python2.5" nil t nil cue3-command-script "-r" "-f" (car (cdr frame)) (car (cdr job)))
      (cue3-update-jobs-list))
     
     ((and job (not frame) (string= "Paused" (car job)) (y-or-n-p (format "Resume job %s " (car (cdr job)))))
      (call-process "python2.5" nil t nil cue3-command-script "-r"  (car (cdr job)))
      (cue3-update-jobs-list)))))

(defun cue3-kill-job-or-frame-at-point ()
  (interactive)
  (let ((frame (cue3-get-frame-at-point))
       (job (cue3-get-nearest-job)))
    (cond
     ((and frame 
           (not (string= "Dead" (car frame)))
           (not (string= "Eaten" (car frame)))
           (y-or-n-p (format "Kill frame %s " (car (cdr frame)))))
      (message "Killing frame %s" (car (cdr frame)))
      (call-process "python2.5" nil (get-buffer "*Messages*") nil cue3-command-script "-k" "-f" (car (cdr frame)) (car (cdr job))))
     
     ((and job (not frame) (y-or-n-p (format "Kill job %s " (car (cdr job)))))
      (message "Killing job %s" (car (cdr job)))
      (call-process "python2.5" nil (get-buffer "*Messages*") nil cue3-command-script "-k"  (car (cdr job)))))

    (cue3-update-jobs-list)))

  
(defun cue3-get-name-at-point ()
  "Get the name of the item (job or frame or nil) at point"
  (interactive)

  (let ((frame (cue3-get-frame-at-point))
       (job (cue3-get-nearest-job)))
    (when job
      (list (car (cdr job)) (car (cdr frame))))))

(defun cue3-get-location (job &optional frame)
  (interactive)
  (when job
    (save-excursion
      (beginning-of-buffer)
      (let ((jobpos (re-search-forward job (point-max) t))
            (framepos nil))
        (when jobpos
          (when frame
            (setq framepos (re-search-forward frame (point-max) t))))
        (if framepos
            framepos
          jobpos)))))

(defun cue3-go-to-job-and-frame (job &optional frame)
  "Expects a list - first item is jobname, second is frame, optionally nil"
  (interactive)
  (beginning-of-buffer)
  (let ((pos (cue3-get-location job frame)))
    (when pos
      (goto-char pos)
      (beginning-of-line))))
            

(defun cue3-goto-expand ()
  (interactive)
  (cue3-go-to-job-and-frame (list cue3-job-expand)))

(defun mode-line-mode-name ()
  (interactive)
  "cue3")

(defun cue3-pause-job-at-point ()
  (interactive)
  (let ((job (or (cue3-get-job-at-point) (cue3-get-nearest-job))))
    (when (and job 
               (not (string= "Paused" (car job)))
               (y-or-n-p (format "Pause job %s " (car (cdr job)))))
      (call-process "python2.5" nil t nil cue3-command-script "-p" (car (cdr job)))
          (cue3-update-jobs-list))))

(defun cue3-get-frame-log ()
  (interactive)
  (let ((frame (cue3-get-frame-at-point))
        (job (cue3-get-nearest-job)))
    (when frame
      (let ((buf (get-buffer-create (concat "*-" (car (cdr job)) "-" (car(cdr frame)) "-logfile-*") )))
	(set-buffer buf)
	(erase-buffer)
	(insert (call-process "python2.5" nil t nil cue3-command-script "-g" "-f" (car (cdr frame)) (car (cdr job))))
	(switch-to-buffer buf)))))


(defun cue3-kill-all-log-buffers ()
  "Kills all buffers visiting log files"
  (interactive)
  (let ((bufList (buffer-list)))
    (while bufList
      (let ((fileName (buffer-file-name (car bufList))))
        (if (and fileName (string-match "/shots/.*/.*/logs" fileName))
            (kill-buffer (car bufList)))
          
      (setq bufList (cdr bufList))))))


(defun cue3-get-cue-dir-from-jobname (jobName)
 (interactive)
 ;(message "JB: %s" jobName)
 (let ((idx (string-match "\\([a-z]+\\)-\\([a-z0-9\\.]+\\)-\\([a-z]+\\)_\\([a-z0-9]+\\)_\\([a-z0-9\\._]+\\)" jobName)))
   (cond (idx
          (let ((show (match-string 1 jobName))
                (shot (match-string 2 jobName))
                (user (match-string 3 jobName))
                (jobtype (match-string 4 jobName))
                (jobbase (match-string 5 jobName)))
            ;(message "Show: %s  Shot: %s  User: %s Type: %s Job: %s" show shot user jobtype jobbase)
            (concat "/shots/" show "/" shot "/cue/" user "/[a-z0-9]+" jobbase)
            ;(message "Dir: %s" (concat "/shots/" show "/" shot "/cue/" user))
            ;(message "Match: %s" (concat "[a-z0-9_]+" jobbase))
            ;(directory-files (concat "/shots/" show "/" shot "/cue/" user))
            (car (directory-files (concat "/shots/" show "/" shot "/cue/" user) t (concat "[a-z0-9_]+" jobbase))))))))


(defun cue3-get-lfxprep-globals-from-job (jobName)
;(interactive)
(let ((cuedir (cue3-get-cue-dir-from-jobname jobName)))
 (when cuedir
   (let ((gblfile (concat cuedir "/globals/lfxprep_archive.xml")))
    (find-file-other-window gblfile)))))


(defun cue3-find-globals-file-other-window ()
(interactive)
(let ((job (or (cue3-get-job-at-point) (cue3-get-nearest-job))))
 (when job
   (let ((gbls (cue3-get-lfxprep-globals-from-job (car (cdr job)))))
     (find-file-other-window gbls)))))


(defun cue3-dired-job-at-point-other-window ()
  (interactive)
  (let ((job (or (cue3-get-job-at-point) (cue3-get-nearest-job))))
    (when job
      (let ((cuedir (cue3-get-cue-dir-from-jobname (car (cdr job)))))
        (when cuedir
          (dired-other-window cuedir))))))

(defun cue3-get-ssu-from-jobname (name)
  (let ((match (string-match "\\([a-z0-9]+\\)-\\([a-z\.0-9]+\\)-\\([a-z0-9]+\\)" name)))
   (if match
     (cons (match-string 1 name) ()))))



(defun cue3-make-face (face color &optional bold)
  (make-face face)
  (copy-face 'default face)
  (set-face-foreground face color)
  (if bold (make-face-bold face)))

(cue3-make-face 'cue3-error-face "firebrick" t)
(cue3-make-face 'cue3-paused-face "orange" t)
(cue3-make-face 'cue3-running-face "medium sea green")
(cue3-make-face 'cue3-depend-face "medium orchid")
(cue3-make-face 'cue3-waiting-face "cornflower blue")
(cue3-make-face 'cue3-succeeded-face "SkyBlue4")
(cue3-make-face 'cue3-eaten-face "firebrick3")
(cue3-make-face 'cue3-watch-face "pale green")

(unless cue3-mode-map
  (setq cue3-mode-map (make-sparse-keymap))
  (define-key cue3-mode-map "r" 'cue3-retry-or-resume-at-point)
  (define-key cue3-mode-map "p" 'cue3-pause-job-at-point)
  (define-key cue3-mode-map (kbd "RET") 'cue3-expand-job-at-point)
  (define-key cue3-mode-map "l" 'cue3-get-frame-log)
  (define-key cue3-mode-map "u" 'cue3-update-jobs-list)
  (define-key cue3-mode-map "k" 'cue3-kill-job-or-frame-at-point)
  (define-key cue3-mode-map "x" 'cue3-eat-frame-at-point)
  (define-key cue3-mode-map "a" 'cue3-retry-all-dead-frames-at-point)
  (define-key cue3-mode-map "w" 'cue3-set-watch)
  (define-key cue3-mode-map "\C-w" 'cue3-set-watch-term)
  (define-key cue3-mode-map "d" 'cue3-drop-depends-frame-at-point)
  (define-key cue3-mode-map "i" 'cue3-itview-job-outputs-at-point)
  (define-key cue3-mode-map "t" 'cue3-test)
  (define-key cue3-mode-map "c" 'cue3-comment-job-at-point)
  (define-key cue3-mode-map "e" 'cue3-eat-frame-at-point))


(defun cue3-mode ()
  (interactive)
  (kill-all-local-variables)
  (setq major-mode 'cue3-mode)
  (setq mode-name "Cue3")
  (use-local-map cue3-mode-map)
  (font-lock-mode)
  (run-hooks 'cue3-mode-hook)
  (setq myKeywords '(
            ("\\(+\\|-\\).*Running.*" . 'cue3-running-face)
            ("\\(+\\|-\\).*Failing.*" . 'cue3-error-face)
            ("\\(+\\|-\\).*Eaten.*" . 'cue3-eaten-face)
            ("\\(+\\|-\\).*Dead.*" . 'cue3-error-face)
            ("\\(+\\|-\\).*Depend.*" . 'cue3-depend-face)
            ("\\(+\\|-\\).*Waiting.*" . 'cue3-waiting-face)
            ("\\(+\\|-\\).*Succeeded.*" . 'cue3-succeeded-face)
            ("\\(+\\|-\\).*Paused.*" . 'cue3-paused-face)
            
))
  (setq font-lock-defaults '(myKeywords))
)

(provide 'cue3)

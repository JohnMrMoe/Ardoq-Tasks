;; Supplement for Ardoq task:
;; Task 1
;
; Create a method that, given a list of integers, returns the highest product
; between 3 of those numbers. Example:
; [1, 10, 2, 6, 5, 3] = 300
;
; This is written in Scheme, so it can be fired in a DrRacket engine
;
; In scheme, a list can be made using the syntax either "(list <e#1> <e#2> <e#3> ... <e#n>)" or " '(<e#1> <e#2> <e#3> ... <e#n>)"

(define (ArdoqTertMux ls)
  (define (mult lis n)
    (if (or (= n 3) (null? lis))
        1
        (* (car lis) (mult (cdr lis) (+ n 1)))))
  (define (assemble3 n1 n2 n3)
      (cond
        ((and (> n1 n2) (> n1 n3)); n1 is the biggest
         (if (> n2 n3)
             (list n1 n2 n3)
             (list n1 n3 n2)))
        ((and (> n2 n1) (> n2 n3)); n2 is the biggest
         (if (> n1 n3)
             (list n2 n1 n3)
             (list n2 n3 n1)))
        (else ;                     n3 is the biggest
         (if (> n1 n2)
             (list n3 n1 n2)
             (list n3 n2 n1)))))
  (define (compareTo3 top3 num); see how high this num is
    (if (< num (caddr top3))
        top3
        (cond
          ((> num (car top3)) (list num (car top3) (cadr top3)))
          (else (list (car top3) num (cadr top3))))))
  (define (scour ls tops)
    (if (null? ls)
        tops
        (scour (cdr ls) (compareTo3 tops (car ls)))))
  (cond
    ((null? ls) 0)
    ((> (length ls) 2)
     (let ((top3 (assemble3 (car ls) (cadr ls) (caddr ls))))
       (mult (scour (cdddr ls) top3) 0)))
    (else (mult ls 0)))
  )

(display "As in example: (1 10 2 6 5 3) = ")
(ArdoqTertMux (list 1 10 2 6 5 3))
(display "Other arrays: (3 6) = ")
(ArdoqTertMux (list 3 6))
(display "Other arrays: (ø) = ")
(ArdoqTertMux '())
(display "Other arrays: (1) = ")
(ArdoqTertMux (list 1))
(display "Other arrays: (23 10 12 9 6 12) = ")
(ArdoqTertMux (list 23 10 12 9 6 12))
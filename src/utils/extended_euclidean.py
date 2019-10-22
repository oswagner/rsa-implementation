# function extended_gcd(a, b)
#     s <- 0;    old_s <- 1
#     t <- 1;    old_t <- 0
#     r <- b;    old_r <- a
#     while r ≠ 0
#         quotient <- old_r div r
#         (old_r, r) <- (r, old_r - quotient * r)
#         (old_s, s) <- (s, old_s - quotient * s)
#         (old_t, t) <- (t, old_t - quotient * t)
#     output "Bézout coefficients:", (old_s, old_t)
#     output "greatest common divisor:", old_r
#     output "quotients by the gcd:", (t, s)


def evaluate_extended_gcd(x, y):
    pass


def xgcd(a, b):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy

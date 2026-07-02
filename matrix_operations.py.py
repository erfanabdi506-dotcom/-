# matrix_operations.py
# عملیات روی ماتریس‌ها (آرایه دو بعدی)

# تعریف دو ماتریس ۲x۲
a = [[0.30, 0.60],
     [0.10, 0.50]]

b = [[0.50, 0.10],
     [0.40, 0.60]]

n = len(a)  # تعداد سطرها

# 1. جمع ماتریس
c_sum = [[0.0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        c_sum[i][j] = a[i][j] + b[i][j]

print("جمع ماتریس‌ها:")
for row in c_sum:
    print(row)

# 2. ضرب ماتریس
c_mul = [[0.0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            c_mul[i][j] += a[i][k] * b[k][j]

print("ضرب ماتریس‌ها:")
for row in c_mul:
    print(row)
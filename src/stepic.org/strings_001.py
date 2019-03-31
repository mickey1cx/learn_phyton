# https://stepik.org/lesson/3367/step/3?unit=950

# sample - "acggtgttat"
genom = input()
count_c = genom.lower().count('c')
count_g = genom.lower().count('g')
summary_gc = (count_c + count_g) / len(genom) * 100
print(summary_gc)

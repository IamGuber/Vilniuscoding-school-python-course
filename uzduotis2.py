# Savo nuožiūra atlikite dar bent vieną analogišką užduotį.

info = ["pirmas", "antras", "trecias", "astuntas", "desimtas", "vienuoliktas"]
print(set(info))
info2 = ["trecias", "ketvirtas", "penktas", "astuntas", "devintas", "vienuoliktas"]
print(set(info2))
info3 = ["septintas", "antras", "ketvirtas", "sestas", "astuntas", "desimtas", "dvyliktas", "septintas"]
print(set(info3))

print()
print()
new_info = set(info)
new_info2 = set(info2)
new_info3 = set(info3)

unikalus_skc = new_info | new_info2 | new_info3
visur_kartojasi = new_info & new_info2 & new_info3

print(unikalus_skc)
print()
print(visur_kartojasi)
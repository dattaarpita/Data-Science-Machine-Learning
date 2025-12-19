defaults={"theme":"light","audio":"on"}
user_pref={"theme":"dark"}

#merge dict using .update()
defaults.update(user_pref)
print(defaults)

#merge dict using | operator
merged_dict=defaults|user_pref
print(merged_dict)
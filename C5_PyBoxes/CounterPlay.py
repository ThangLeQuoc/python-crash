from collections import Counter

breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())

lunch = ['eggs','eggs','bacon']
lunch_counter = Counter(lunch)

print(breakfast_counter + lunch_counter)

# get common thing
print(breakfast_counter & lunch_counter)

# get union
print(breakfast_counter | lunch_counter)
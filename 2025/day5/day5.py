data = open("./day5/input.txt", "r").read().splitlines()

ingredients = []
fresh_ranges = []

whiteline = False
for line in data:
    if line == "":
        whiteline = True
        continue
    
    if whiteline:
        ingredients.append(int(line))
        continue
    
    n,m =line.split("-")
    fresh_ranges.append([int(n), int(m)])


def merge_fresh_range_set(fresh_ranges):
    fresh_ranges = sorted(fresh_ranges)

    fresh_range_sets = []
    for fresh_range in fresh_ranges:
        start = fresh_range[0]
        end = fresh_range[1]

        current_set = [start, end]
        if len(fresh_range_sets) == 0:
            fresh_range_sets.append(current_set)
            continue
            
        previous_set = fresh_range_sets[len(fresh_range_sets) - 1]

        # Check intersection
        if previous_set[1] >= current_set[0]:
            # merge sets
            merged_set = [min(current_set[0], previous_set[0]), max(previous_set[1], current_set[1])]
            fresh_range_sets[len(fresh_range_sets) - 1] = merged_set
        else:
            fresh_range_sets.append(current_set)

    return fresh_range_sets
        
def read_freshness(ingredient, fresh_ranges):
    for fresh_range in fresh_ranges:
        if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
            return True
    return False



p1_fresh_ingredients = 0
fresh_ranges = merge_fresh_range_set(fresh_ranges)

for ingredient in ingredients:
    is_fresh = read_freshness(ingredient, fresh_ranges)
    if is_fresh:
        p1_fresh_ingredients += 1


p2_count_all_Fresh_Id = 0
for fresh_range in fresh_ranges:
    p2_count_all_Fresh_Id += (fresh_range[1] - fresh_range[0] + 1)

print(p1_fresh_ingredients)
print(p2_count_all_Fresh_Id)
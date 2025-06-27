# Problem 1: Brand Filter
def filter_sustainable_brands(brands, criterion):
    ans = []
    for i in brands:
        if criterion in i.get("criteria"):
            ans.append(i.get('name'))
    return ans

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))


# Problem 2: Eco-Friendly Materials
def count_material_usage(brands):
    ans = {}
    for i in brands:
        for j in i.get("materials"):
            if j in ans:
                ans[j] += 1
            else:
                ans[j] = 1

    return ans         

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))


# Problem 3: Fashion Trends
def find_trending_materials(brands):
    dict1 = {}
    ans = []
    for i in brands:
        for j in i.get("materials"):
            if j in dict1:
                dict1[j] += 1
            else:
                dict1[j] = 1
    for key, value in dict1.items():
        if value > 1:
            ans.append(key)

    return ans

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(find_trending_materials(brands))
# print(find_trending_materials(brands_2))
# print(find_trending_materials(brands_3))

# Problem 4: Fabric Pairing
def find_best_fabric_pair(fabrics, budget):
    fabrics.sort(key=lambda x: x[1])
    left = 0
    right = len(fabrics) - 1
    max_sum = float('-inf')
    best_pair = None

    while left < right:
        current_sum = fabrics[left][1] + fabrics[right][1]

        if current_sum == budget:
            return (fabrics[left][0], fabrics[right][0])
            
        elif current_sum < budget and current_sum > max_sum:
            max_sum = current_sum
            best_pair = (fabrics[left][0], fabrics[right][0])
            leftt += 1
        elif current_sum > budget:
            right -= 1
        else:
            left += 1

    return best_pair


fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

# print(find_best_fabric_pair(fabrics, 45))
# print(find_best_fabric_pair(fabrics_2, 70))
# print(find_best_fabric_pair(fabrics_3, 60))

# Problem 5: Fabric Stacks
def organize_fabrics(fabrics):
    fabrics.sort(key=lambda x: x[1], reverse=True)
    ans = []
    for i in fabrics:
        ans.append(i[0])
    return ans
    
fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))



def process_supplies(supplies):
    supplies.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in supplies]

supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))


def calculate_fabric_waste(items, fabric_rolls):
    pass


items = [("T-Shirt", 2), ("Pants", 3), ("Jacket", 5)]
fabric_rolls = [5, 5, 5]

items_2 = [("Dress", 4), ("Skirt", 3), ("Blouse", 2)]
fabric_rolls = [4, 4, 4]

items_3 = [("Jacket", 6), ("Shirt", 2), ("Shorts", 3)]
fabric_rolls = [7, 5, 5]

print(calculate_fabric_waste(items, fabric_rolls))
print(calculate_fabric_waste(items_2, fabric_rolls))
print(calculate_fabric_waste(items_3, fabric_rolls))


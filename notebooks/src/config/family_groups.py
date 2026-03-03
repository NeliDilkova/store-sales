
family_to_group = {
    # Grocery I allein
    "GROCERY I": "grocery_I",

    # Top volume food
    "BEVERAGES": "top_volume_food",
    "PRODUCE": "top_volume_food",

    # High Volume Food
    "BREAD/BAKERY": "high_volume_food",
    "DAIRY": "high_volume_food",
    "DELI": "high_volume_food",
    "POULTRY": "high_volume_food",
    "EGGS": "high_volume_food",
    "CLEANING": "high_volume_food",

    # Low Volume Food
    "MEATS": "low_volume_food",
    "SEAFOOD": "low_volume_food",
    "PREPARED FOODS": "low_volume_food",

    # Mid Volume Mixed
    "HOME CARE": "mid_volume_mixed",
    "BABY CARE": "mid_volume_mixed",
    "PERSONAL CARE": "mid_volume_mixed",
    "PET SUPPLIES": "mid_volume_mixed",
    "HOME AND KITCHEN I": "mid_volume_mixed",
    "HOME AND KITCHEN II": "mid_volume_mixed",
    "HOME APPLIANCES": "mid_volume_mixed",
    "BEAUTY": "mid_volume_mixed",
    "LADIESWEAR": "mid_volume_mixed",
    "LAWN AND GARDEN": "mid_volume_mixed",
    "PLAYERS AND ELECTRONICS": "mid_volume_mixed",
    "CELEBRATION": "mid_volume_mixed",
    "MAGAZINES": "mid_volume_mixed",
    "BOOKS": "mid_volume_mixed",

    # Low volume mixed
    "FROZEN FOODS": "low_volume_mixed",
    "SCHOOL AND OFFICE SUPPLIES": "low_volume_mixed",
    "GROCERY II": "low_volume_mixed",

    # Low Volume / Special / Fashion / Media
    "HARDWARE": "low_volume_special",
    "AUTOMOTIVE": "low_volume_special",
    "LINGERIE": "low_volume_special",
    "LIQUOR,WINE,BEER": "low_volume_special",
}


def add_family_group(df):
    df = df.copy()
    df["family_group"] = df["family"].map(family_to_group).fillna("other_family")
    return df

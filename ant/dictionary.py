monthdictionary = {
    "jan":"january",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may":"may",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sep":"september",
    "oct":"october",
    "nov":"november",
    "dec":"december"
}
key = input("input the keyword :")

print(monthdictionary.get(key,"invalid keyword"))

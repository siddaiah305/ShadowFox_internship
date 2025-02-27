a=input("enter first city")
b=input("enetr second city")
country = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}
if a in country and b in country:
   if country[a]==country[b]:
      print(f"Both cities are in {country[a]}")
else:
    print("Both countries are not in the same country")
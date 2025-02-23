import data
from data import CountyDemographics
from build_data import get_data


def population_total(lst:list[CountyDemographics]) -> int:
    population_total = 0
    for county in lst:
        population_total += county.population.get('2014 Population')
    return population_total
#-----------------------------------
def filter_by_state(lst:list[CountyDemographics], state: str) -> list[CountyDemographics]:
    county_in_state = []
    for county in lst:
        if county.state == state:
            county_in_state.append(county)
    return county_in_state
#-------------------------------------

def population_by_education(lst:list[CountyDemographics], key:str):
    population = 0.0
    for county in lst:
        if key in county.education:
            population += county.population.get('2014 Population') * (county.education.get(key)/100)
    return float(population)

def population_by_ethnicity(lst:list[CountyDemographics], key:str):
    population = 0.0
    for county in lst:
        if key in county.ethnicities:
            population += county.population.get('2014 Population') * (county.ethnicities.get(key)/100)
    return float(population)

def population_below_poverty_line(lst:list[CountyDemographics], key:str):
    population = 0.0
    for county in lst:
        if key in county.income:
            population += county.population.get('2014 Population') * (county.income.get(key)/100)
    return float(population)
#---------------------------------------------

def percent_by_education(lst:list[CountyDemographics], key:str) -> float:
    total = population_total(lst)
    subtotal = population_by_education(lst,key)
    return (subtotal/total) * 100

def percent_by_ethnicity(lst:list[CountyDemographics], key:str) -> float:
    total = population_total(lst)
    subtotal = population_by_ethnicity(lst,key)
    return (subtotal/total) * 100

def percent_below_poverty_level(lst:list[CountyDemographics], key:str) -> float:
    total = population_total(lst)
    subtotal = population_below_poverty_line(lst,key)
    return (subtotal/total) * 100
#-------------------------------------------------------------
def education_greater_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.education[key] > threshold:
            final.append(county)
    return final

def education_lesser_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.education[key] < threshold:
            final.append(county)
    return final

def ethnicity_greater_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.ethnicities[key] > threshold:
            final.append(county)
    return final

def ethnicity_lesser_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.ethnicities[key] < threshold:
            final.append(county)
    return final

def below_poverty_level_greater_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.income[key] > threshold:
            final.append(county)
    return final
def below_poverty_level_lesser_than(lst:list[CountyDemographics], key:str, threshold:float) -> list[CountyDemographics]:
    final = []
    for county in lst:
        if county.income[key] < threshold:
            final.append(county)
    return final

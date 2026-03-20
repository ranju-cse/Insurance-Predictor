from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Literal,Annotated
from config.city_tier import Tier_1,Tier_2

#Pydantic model to validate incoming data
class User(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of user')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of user')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='Height of user')]
    income_lpa:Annotated[float,Field(...,gt=0,description='Annual Salary of user in lpa')]
    smoker:Annotated[bool,Field(...,description='Is user smoke')]
    city:Annotated[str,Field(...,description='City of user')]
    occupation:Annotated[Literal['retired','freelancer','student','government_job','buisness_owner','unemployed','private_job'],Field(...,description='Occupation of user')]

    @field_validator('city')
    @classmethod
    def normalize_city(cls,v:str)->str:
        v=v.strip().title()#remove extra whitespace
        return v

    
    @computed_field
    @property
    def bmi(self)-> float:
        return round(self.weight/(self.height**2),2)
    
    #Lifestyle Risk
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker or self.bmi > 30:
         return "high"
        elif self.bmi > 27:
         return "medium"
        else:
          return "low"
        
    #Age Group
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return 'young'
        elif  self.age>45:
            return "adult"
        elif self.age> 60:
         return "middle_aged"
        else:
            return "senior"
     
        
    #City Tier
    @computed_field
    @property
    def city_tier(self)->str:
        if self.city in Tier_1:
            return 1
        elif self.city in Tier_2:
            return 2
        else:
            return 3
        
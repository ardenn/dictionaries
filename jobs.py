#Define a Job Class
class Job:
    def __init__(self,
                 title="Job Title",
                 location="Job Location",
                 job_type="Job Type",
                 employer="Job Employer",
                 category="Job Category",):       
        self.title = title
        self.location = location
        self.job_type = job_type
        self.employer = employer
        self.category = category
    def __str__(self):
        return self.title
    
#Defining Job2 class with an extra field
class Job2:
    def __init__(self,
                 title="Job Title",
                 location="Job Location",
                 job_type="Job Type",
                 employer="Job Employer",
                 category="Job Category",
                 salary=50000):               
        self.title = title
        self.location = location
        self.job_type = job_type
        self.employer = employer
        self.category = category
        self.salary = salary
    def __str__(self):
        return self.title

#Defining Job3 class with two extra fields
class Job3:
    def __init__(self,
                 title="Job Title",
                 location="Job Location",
                 job_type="Job Type",
                 employer="Job Employer",
                 category="Job Category",
                 salary=50000,
                 extra_field="A new field"):               
        self.title = title
        self.location = location
        self.job_type = job_type
        self.employer = employer
        self.category = category
        self.salary = salary
        self.extra_field = extra_field
    def __str__(self):
        return self.title
class Config:
    __PopulationSize = 50 # Population Size
    __MaxDomain = 1 # variable upper limit
    __MinDomain = 0 # variable lower limit
    __Lambda = 1.5 # parameter for Levy flight
    __Pa = 0.25
    __Step_Size = 0.01
    __Dimension = 10 # The number of dimension
    __Trial = 31
    __Iteration = 3000
    __Seed = 0
    __Cost = []
    __Restrictions = []
    __Mandatory = []
    __Constrains = []

    @classmethod
    def get_Constrains(cls):
        return cls.__Constrains
    @classmethod
    def set_Constrains (cls, _constrains):
        cls.__Constrains = _constrains 
    
    
    @classmethod
    def get_Mandatory(cls):
        return cls.__Mandatory
    @classmethod
    def set_Mandatory(cls, _mandatory):
        cls.__Mandatory = _mandatory

    @classmethod
    def get_Restrictions(cls):
        return cls.__Restrictions
    @classmethod
    def set_Restrictions(cls, _restrictions):
        cls.__Restrictions = _restrictions

    @classmethod
    def get_Cost(cls):
        return cls.__Cost
    @classmethod
    def set_Cost(cls, _cost):
        cls.__Cost = _cost

    @classmethod
    def get_Seed(cls):
        return cls.__Seed
    @classmethod
    def set_Seed(cls, _seed):
        cls.__Seed = _seed
        
    @classmethod
    def get_population_size(cls):
        return cls.__PopulationSize
    @classmethod
    def set_population_size(cls, _populationSize):
        cls.__PopulationSize = _populationSize
        
        
    @classmethod
    def get_Pa(cls):
        return cls.__Pa
    @classmethod
    def set_Pa(cls, _pA):
        cls.__Pa = _pA

    @classmethod
    def get_iteration(cls):
        return cls.__Iteration  
    @classmethod
    def set_iteration(cls, _iterations):
        cls.__Iteration = _iterations
        
    @classmethod
    def get_trial(cls):
        return cls.__Trial
    @classmethod
    def set_trial(cls, _trial):
        cls.__Trial = _trial
        
        
    @classmethod
    def get_dimension(cls):
        return cls.__Dimension
    @classmethod
    def set_dimension(cls, _dimension):
        cls.__Dimension = _dimension

    @classmethod
    def get_max_domain(cls):
        return cls.__MaxDomain
    @classmethod
    def set_max_domain(cls, _max_domain):
        cls.__MaxDomain = _max_domain

    @classmethod
    def get_min_domain(cls):
        return cls.__MinDomain
    @classmethod
    def set_min_domain(cls, _min_domain):
        cls.__MinDomain = _min_domain

    @classmethod
    def get_lambda(cls):
        return cls.__Lambda
    @classmethod
    def set_lambda(cls, _lambda):
        cls.__Lambda = _lambda

    @classmethod
    def get_stepsize(cls):
        return cls.__Step_Size
    @classmethod
    def set_stepsize(cls, _stepSize):
        cls.__Step_Size = _stepSize
    


    




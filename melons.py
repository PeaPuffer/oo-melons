"""Classes for melon orders."""


class AbstractMelonOrder(): #This of this as BASE Order~
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False 


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
    
#------------------------------------------------------------------------------
        # self.species = species
        # self.qty = qty
        # self.shipped = False #NOT IN ATTRIBUTES, but needs to be in main?
#------------------------------------------------------------------------------

        self.order_type = "domestic" 
        self.tax = 0.08 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code)
        
#------------------------------------------------------------------------------
        # self.species = species
        # self.qty = qty
        # self.shipped = False #NOT IN ATTRIBUTES, but needs to be in main?
#------------------------------------------------------------------------------

        self.order_type = "international" #Is this needed after AbstractMelonOrder?
        self.country_code = country_code #++++This is InternationalMelonOrder specific
        self.tax = 0.17 #++++This is InternationalMelonOrder specific

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
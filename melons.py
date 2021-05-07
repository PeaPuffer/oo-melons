# """Classes for melon orders."""


# class AbstractMelonOrder(): #This of this as BASE Order~
#     """An abstract base class that other Melon Orders inherit from."""

#     def __init__(self, species, qty, country_code = None):
#         self.species = species
#         self.qty = qty
#         self.shipped = False 


# class GovernmentMelonOrder(AbstractMelonOrder):
#         # """Melon Inspection."""

#     def __init__(self, species, qty):
#         super().__init__(species, qty)
#         # """Initialize melon order attributes."""

#         self.passed_inspection = False
        
#     def mark_inspection(self):
#         self.passed_inspection = True


#     def get_total(self):
#         """Calculate price, there's no tax."""

#         base_price = 5 

#         total = self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class DomesticMelonOrder(AbstractMelonOrder):
#     """A melon order within the USA."""

#     def __init__(self, species, qty):
#         super().__init__(species, qty)
#         """Initialize melon order attributes."""

#         self.order_type = "domestic" 
#         self.tax = 0.08 

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True


# class InternationalMelonOrder(AbstractMelonOrder):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         super().__init__(species, qty, country_code)
#         """Initialize melon order attributes."""

#         self.order_type = "international" #Is this needed after AbstractMelonOrder?
#         self.country_code = country_code #++++This is InternationalMelonOrder specific
#         self.tax = 0.17 #++++This is InternationalMelonOrder specific

#     def get_total(self):
#         """Calculate price, including tax."""

#         base_price = 5 * (1.5)

#         total = (1 + self.tax) * self.qty * base_price

#         if self.qty < 10:
#             total += 5

#         return total

#     def mark_shipped(self):
#         """Record the fact than an order has been shipped."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code


#*************************************************************************************

"""Classes for melon orders."""


class AbstractMelonOrder(): 
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False 
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            if self.qty < 10:
                total += 3

        elif self.order_type == "government":
            total = self.qty * base_price

        if self.species == "christmas melon":
            base_price = (base_price * 1.5)
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
        # """Melon Inspection."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        # """Initialize melon order attributes."""

        self.order_type = "government" 
        self.passed_inspection = False
        self.tax = 0.00
        
    def mark_inspection(self):
        self.passed_inspection = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""

        self.order_type = "domestic" 
        self.tax = 0.08 


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, country_code)
        """Initialize melon order attributes."""

        self.order_type = "international" 
        self.country_code = country_code 
        self.tax = 0.17 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
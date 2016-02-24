# -*- coding: utf-8 -*-

"""
   BaseJsonLib.Models.WriteCareerSerializer
 
   This file was automatically generated by APIMATIC BETA v2.0 on 02/24/2016
"""
from BaseJsonLib.APIHelper import APIHelper

class WriteCareerSerializer(object):

    """Implementation of the 'WriteCareerSerializer' model.

    TODO: type model description here.

    Attributes:
        company_name (string): TODO: type description here.
        job_title (string): TODO: type description here.
        description (string): TODO: type description here.
        from_date (DateTime): TODO: type description here.
        to_date (DateTime): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the WriteCareerSerializer class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    company_name -- string -- Sets the attribute company_name
                    job_title -- string -- Sets the attribute job_title
                    description -- string -- Sets the attribute description
                    from_date -- DateTime -- Sets the attribute from_date
                    to_date -- DateTime -- Sets the attribute to_date
        
        """
        # Set all of the parameters to their default values
        self.company_name = None
        self.job_title = None
        self.description = None
        self.from_date = None
        self.to_date = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "company_name": "company_name",
            "job_title": "job_title",
            "description": "description",
            "from_date": "from_date",
            "to_date": "to_date",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "company_name": "company_name",
            "job_title": "job_title",
            "description": "description",
            "from_date": "from_date",
            "to_date": "to_date",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)
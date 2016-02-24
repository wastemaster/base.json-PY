# -*- coding: utf-8 -*-

"""
   BaseJsonLib.Models.WriteSkillSerializer
 
   This file was automatically generated by APIMATIC BETA v2.0 on 02/24/2016
"""
from BaseJsonLib.APIHelper import APIHelper

class WriteSkillSerializer(object):

    """Implementation of the 'WriteSkillSerializer' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        category (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the WriteSkillSerializer class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    name -- string -- Sets the attribute name
                    category -- string -- Sets the attribute category
        
        """
        # Set all of the parameters to their default values
        self.name = None
        self.category = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "name": "name",
            "category": "category",
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
            "name": "name",
            "category": "category",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)
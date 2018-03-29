# -*- coding: utf-8 -*-


{
    "name" : "Multi Image",
    "version" : "2.0",
    "author": "Serpent Consulting Services Pvt. Ltd. migrated to V8 by EL HARTI Mohamed Charif",
    "website": "http://www.serpentcs.com",
    "category": 'Image',
    'depends': ['base'],
    "description": """
        This module provides the functionality to store multiple images for one record.
        All images store in server directory. so database size does not increase.
    """,
    'data': [
     'import.xml',
       
        
    ],
    'qweb': ['static/src/xml/image_multi.xml'],
    'installable': True,
}
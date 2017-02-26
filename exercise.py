# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:36:09 2017

@author: Dell
"""

class SMS_store:
    def __init__(self,has_been_view,from_number,time_arrived,text_of_sms):
        self.has_been_view=has_been_view
        self.from_number=from_number
        self.time_arrived=time_arrived
        self.text_of sms=text_of_sms

    
    
    
    
    
    

class Message:
    def __init__(self,has_been_view,from_number,time_arrived,text_of_sms):
        self._has_been_view=has_been_view
        self._from_number=from_number
        self._time_arrived=time_arrived
        self._text_of_sms=text_of_sms
        
    def viewing(self):
        
        
    
    def sender(self):
        return self._from_number
    def time_arrival(self):
        return self._time_arrived
    def content(self):
        return self._text_of_sms
    
        
        
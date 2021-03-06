'''
Copyright (c) 2008-2015 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Multi Hop Feature enable or disable resource
'''

class multihop_feature(base_resource):
	_enable= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "multihop_feature"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "multihop_features"
		except Exception as e :
			raise e



	'''
	get Enable web insight data record logging value
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set Enable web insight data record logging value
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e

	'''
	To set data record logging value.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				multihop_feature_obj= multihop_feature()
				return cls.perform_operation_bulk_request(service,"add", resource,multihop_feature_obj)
		except Exception as e :
			raise e

	'''
	To get data record logging value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				multihop_feature_obj=multihop_feature()
				response = multihop_feature_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set data record logging value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				multihop_feature_obj=multihop_feature()
				return cls.update_bulk_request(client,resource,multihop_feature_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of multihop_feature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			multihop_feature_obj = multihop_feature()
			option_ = options()
			option_._filter=filter_
			return multihop_feature_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the multihop_feature resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			multihop_feature_obj = multihop_feature()
			option_ = options()
			option_._count=True
			response = multihop_feature_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of multihop_feature resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			multihop_feature_obj = multihop_feature()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = multihop_feature_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(multihop_feature_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.multihop_feature
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(multihop_feature_responses, response, "multihop_feature_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.multihop_feature_response_array
				i=0
				error = [multihop_feature() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.multihop_feature_response_array
			i=0
			multihop_feature_objs = [multihop_feature() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_multihop_feature'):
					for props in obj._multihop_feature:
						result = service.payload_formatter.string_to_bulk_resource(multihop_feature_response,self.__class__.__name__,props)
						multihop_feature_objs[i] = result.multihop_feature
						i=i+1
			return multihop_feature_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(multihop_feature,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class multihop_feature_response(base_response):
	def __init__(self,length=1) :
		self.multihop_feature= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.multihop_feature= [ multihop_feature() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class multihop_feature_responses(base_response):
	def __init__(self,length=1) :
		self.multihop_feature_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.multihop_feature_response_array = [ multihop_feature() for _ in range(length)]

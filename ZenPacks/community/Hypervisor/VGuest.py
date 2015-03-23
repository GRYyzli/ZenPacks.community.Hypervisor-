from Globals import InitializeClass
# from AccessControl import ClassSecurityInfo

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import convToUnits
from Products.ZenModel.HWComponent import HWComponent

from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from subprocess import *
import os

_kw = dict(mode='w')

class VGuest (DeviceComponent, ManagedEntity):
	
	portal_type = meta_type = 'Guest'

	severity = ""
	vmName = ""
	vmOS = ""
	vmState = ""
	vmIp = ""
	cpu_usage = ""
	cpu_usagemhz = ""
	cpu_total = ""
	mem_active = ""
	mem_total = ""
	mem_usage = ""
	mem_usagemb = ""
	tools_Status = ""
	vmHD1_name = ""
	vmHD2_name = ""
	vmHD3_name = ""
	vmHD4_name = ""
	vmHD5_name = ""
	vmHD6_name = ""
	vmHD7_name = ""
	vmHD8_name = ""
	vmHD1_size = ""
	vmHD2_size = ""
	vmHD3_size = ""
	vmHD4_size = ""
	vmHD5_size = ""
	vmHD6_size = ""
	vmHD7_size = ""
	vmHD8_size = ""
	vmHD1_datastore = ""
	vmHD2_datastore = ""
	vmHD3_datastore = ""
	vmHD4_datastore = ""
	vmHD5_datastore = ""
	vmHD6_datastore = ""
	vmHD7_datastore = ""
	vmHD8_datastore = ""
	vmHDall = ""
	vmid = ""
	company = ""
	service = ""
	description = ""
	config_file = ""
	oracle_sids = ""

	#status = 0 

    	_properties = (
        	{'id':'severity', 'type':'string', 'mode':'w'},
        	{'id':'vmName', 'type':'string', 'mode':'w'},
        	{'id':'vmIp', 'type':'string', 'mode':'w'},
        	{'id':'vmState', 'type':'string', 'mode':'w'},
        	{'id':'vmOS', 'type':'string', 'mode':'w'},
        	{'id':'tools_Status', 'type':'string', 'mode':'w'},
        	{'id':'cpu_usage', 'type':'string', 'mode':'w'},
        	{'id':'cpu_usagemhz', 'type':'string', 'mode':'w'},
        	{'id':'cpu_total', 'type':'string', 'mode':'w'},
        	{'id':'mem_active', 'type':'string', 'mode':'w'},
        	{'id':'mem_usage', 'type':'string', 'mode':'w'},
        	{'id':'mem_usagemb', 'type':'string', 'mode':'w'},
        	{'id':'mem_total', 'type':'string', 'mode':'w'},
        	#{'id':'status', 'type':'int', 'mode':'w'},
        	{'id':'vmHD1_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD2_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD3_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD4_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD5_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD6_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD7_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD8_name', 'type':'string', 'mode':'w'},
        	{'id':'vmHD1_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD2_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD3_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD4_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD5_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD6_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD7_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD8_size', 'type':'string', 'mode':'w'},
        	{'id':'vmHD1_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD2_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD3_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD4_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD5_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD6_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD7_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHD8_datastore', 'type':'string', 'mode':'w'},
        	{'id':'vmHDall', 'type':'string', 'mode':'w'},
        	{'id':'vmid', 'type':'string', 'mode':'w'},
        	{'id':'company', 'type':'string', 'mode':'w'},
        	{'id':'service', 'type':'string', 'mode':'w'},
        	{'id':'description', 'type':'string', 'mode':'w'},
        	{'id':'config_file', 'type':'string', 'mode':'w'},
        	{'id':'oracle_sids', 'type':'string', 'mode':'w'},
    	)

#	_properties = (
#		dict(id='vmName',		type='string',	**_kw),
#		dict(id='vmIp',			type='string',	**_kw),
#		dict(id='vmOS',		 	type='string',	**_kw),
#		dict(id='vmState',	 	type='string',	**_kw),
#		dict(id='cpu_usage',	 	type='string',	**_kw),
#		dict(id='cpu_usagemhz',	 	type='string',	**_kw),
#		dict(id='mem_active',	 	type='string',	**_kw),
#		dict(id='mem_usage',	 	type='string',	**_kw),
#		dict(id='mem_usagemb',	 	type='string',	**_kw),
#		dict(id='monitored',	 	type='boolean',	**_kw),
#		dict(id='status',   		type='int', 'mode':'w'),
#	)

	_relations = (
		('VDevice', ToOne(ToManyCont, 
		'ZenPacks.community.Hypervisor.VDevice', 
			'VGuest')
		),
	)

	# Screen action bindings (and tab definitions)
	factory_type_information = (
		{
			'id'             : 'VGuest',
			'meta_type'      : 'Virtual Guest',
			'description'    : 'Virtual Guest Description',
			'icon'           : 'Device_icon.gif',
			'product'        : 'VDevice',
			'factory'        : 'manage_addVGuest',
			'immediate_view' : 'vguestPerformance',
			'actions'        :
			(
#				{ 'id'            : 'perf'
#				, 'name'          : 'Graphs'
#				, 'action'        : 'vguestPerformance'
#				, 'permissions'   : (ZEN_VIEW, )
#				},
#				{ 'id'            : 'templates'
#				, 'name'          : 'Templates'
#				, 'action'        : 'objTemplates'
#				, 'permissions'   : (ZEN_CHANGE_SETTINGS, )
#				},
			)
		},
	)

	def device(self):
		return self.VDevice()

	def managedDeviceLink(self):
		from Products.ZenModel.ZenModelRM import ZenModelRM
		d = self.getDmdRoot("Devices").findDevice(self.vmName)
		if d:
			return ZenModelRM.urlLink(d, 'link')
		return None

	#def snmpIgnore(self):
	#	return ManagedEntity.snmpIgnore(self) or self.snmpindex < 0

	#def monitored(self):
	#	if self.vmState == "UP":
        #                return "true" 
	#	return "false"

	
	def getStatusString(self, statClass=None):
        
        #Return a text representation of this component's status
        
		#return "UP"	
		return self.vmState	
	
        #return self.convertStatus(self.getStatus(statClass))
	
	def getStatus(self, statClass=None):
        
        #Return the status number for this component of class statClass.
        
        	#if not self.monitored() \
            	#	or not self.device() \
            	#	or not self.device().monitorDevice(): return -1
		if self.vmState == "UP":
			return 0 
 
		return 1 

        #if not statClass: statClass = "/Status/%s" % self.meta_type
        #return self.getEventManager().getComponentStatus(
        #        self.getParentDeviceName(), self.name(), statclass=statClass)



InitializeClass(VGuest)

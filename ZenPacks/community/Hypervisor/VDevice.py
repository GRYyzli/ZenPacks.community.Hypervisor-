from Globals import InitializeClass
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenRelations.RelSchema import *

from copy import copy

class VDevice(Device):
	"VMWare ESX Server"

	_relations = Device._relations + (
		('VGuest', ToManyCont(ToOne, 
			"ZenPacks.community.Hypervisor.VGuest", "VDevice")),
		) 
	_relations = _relations + (
                ('VDatastore', ToManyCont(ToOne,
                        "ZenPacks.community.Hypervisor.VDatastore", "VDevice")),
                )
	
#	factory_type_information = (
#			{
#				'immediate_view' : 'deviceStatus',
#				'actions'        :
#				(
#					{ 'id'            : 'status'
#					, 'name'          : 'Status'
#					, 'action'        : 'deviceStatus'
#					, 'permissions'   : (ZEN_VIEW, )
#					},
#					#{ 'id'            : 'osdetail'
#                                        #, 'name'          : 'OS'
#                                        #, 'action'        : 'deviceOsDetail'
#                                        #, 'permissions'   : (ZEN_VIEW, )
#                                        #},
#					{ 'id'            : 'vguestData'
#					, 'name'          : 'Virtual Machines'
#					, 'action'        : 'vguestData'
#					, 'permissions'   : (ZEN_VIEW,)
#					},
#					{ 'id'            : 'vdatastoreData'
#                                        , 'name'          : 'Datastores'
#                                        , 'action'        : 'vdatastoreData'
#                                        , 'permissions'   : (ZEN_VIEW,)
#					},
#					{ 'id'            : 'events'
#					, 'name'          : 'Events'
#					, 'action'        : 'viewEvents'
#					, 'permissions'   : (ZEN_VIEW, )
#					},
#					{ 'id'            : 'perfServer'
#					, 'name'          : 'Graphs'
#					, 'action'        : 'viewDevicePerformance'
##					, 'permissions'   : (ZEN_VIEW, )
#					},
#					{ 'id'            : 'edit'
#					, 'name'          : 'Edit'
#					, 'action'        : 'editDevice'
#					, 'permissions'   : ("Change Device",)
#					},
#				)
#			},
#		)
#
#	def buildDeviceTreeProperties(self):
#    		devs = self.getDmdRoot("Devices")
#		devs._setProperty("zVUser", "disit")
#        	devs._setProperty("zVPassword", "haslo123")
#
	def __init__(self, *args, **kw): 
		Device.__init__(self, *args, **kw) 
		self.buildRelations()
      
InitializeClass(VDevice)

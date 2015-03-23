__doc__="VDatastore"

from Globals import InitializeClass
# from AccessControl import ClassSecurityInfo

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import convToUnits

from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from subprocess import *
import os

_kw = dict(mode='w')

class VDatastore(DeviceComponent, ManagedEntity):
        "Datastore Information"

        portal_type = meta_type = 'Datastore'

        vdName = ""
        vdId = ""
        vdTotal = ""
        vdUsed = ""
        vdFree = ""
        vdPercent = ""
        vdFilesystem = ""
        vdVersion = ""
        vdDescription = ""
	vdPath = ""

        _properties = (
                dict(id='vdName',	        type='string',  **_kw),
                dict(id='vdTotal',              type='string',  **_kw),
                dict(id='vdUsed',               type='string',  **_kw),
                dict(id='vdFree',               type='string',  **_kw),
                dict(id='vdPercent',            type='string',  **_kw),
                dict(id='vdFilesystem',            type='string',  **_kw),
                dict(id='vdId',            	type='string',  **_kw),
                dict(id='vdVersion',            type='string',  **_kw),
                dict(id='vdDescription',            type='string',  **_kw),
                dict(id='vdPath',            	type='string',  **_kw),
        )

        _relations = (
                ('VDevice', ToOne(ToManyCont,
                'ZenPacks.community.Hypervisor.VDevice',
                        'VDatastore')
                ),
        )
        # Screen action bindings (and tab definitions)

        factory_type_information = (
                {
                        'id'             : 'VDatastore',
                        'meta_type'      : 'Virtual Datastore',
                        'description'    : 'Virtual Datastore Description',
                        'icon'           : 'Device_icon.gif',
                        'product'        : 'VDevice',
                        'factory'        : 'manage_addVDatastore',
                        'immediate_view' : 'vdatastorePerformance',
                        'actions'        :
                        (
#                                { 'id'            : 'perf'
#                                , 'name'          : 'Graphs'
#                                , 'action'        : 'vdatastorePerformance'
#                                , 'permissions'   : (ZEN_VIEW, )
#                                },
#                                { 'id'            : 'templates'
#                                , 'name'          : 'Templates'
#                                , 'action'        : 'objTemplates'
#                                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
#                                },
                        )
                },
        )

        def device(self):
                return self.VDevice()


        def snmpIgnore(self):
                return ManagedEntity.snmpIgnore(self) or self.snmpindex < 0

	

InitializeClass(VDatastore)


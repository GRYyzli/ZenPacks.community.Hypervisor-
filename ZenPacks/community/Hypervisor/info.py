################################################################################
#
# This program is part of the deviceAdvDetail Zenpack for Zenoss.
# Copyright (C) 2008, 2009, 2010 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of Data Source.

#$Id: info.py,v 1.0 2010/06/24 12:32:04 egor Exp $"""

__version__ = "$Revision: 1.0 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import ThresholdInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.community.Hypervisor import interfaces

class VGuestInfo(ComponentInfo):
    implements(interfaces.IVGuestInfo)

    vmName = ProxyProperty("vmName")
    vmIp = ProxyProperty("vmIp")
    vmOS = ProxyProperty("vmOS")
    vmState = ProxyProperty("vmState")
    cpu_total = ProxyProperty("cpu_total")
    mem_total = ProxyProperty("mem_total")
    vmHDall = ProxyProperty("vmHDall")
    company = ProxyProperty("company")
    service = ProxyProperty("service")

    #@property
    #def status(self):
        #if not hasattr(self._object, 'vmState'): return 'Unknown'
        #else: return self._object.vmState()
        #return self._object.vmState()

class VDatastoreInfo(ComponentInfo):
    implements(interfaces.IVDatastoreInfo)

    vdName = ProxyProperty("vdName")
    vdTotal = ProxyProperty("vdTotal")
    vdUsed = ProxyProperty("vdUsed")
    vdFree = ProxyProperty("vdFree")
    vdFilesystem = ProxyProperty("vdFilesystem")
    vdVersion = ProxyProperty("vdVersion")
    vdPath = ProxyProperty("vdPath")


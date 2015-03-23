#s program is part of the deviceAdvDetail Zenpack for Zenoss.
# Copyright (C) 2008, 2009, 2010 Egor Puzanov.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

$Id: interfaces.py,v 1.1 2010/07/07 13:37:53 egor Exp $"""

__version__ = "$Revision: 1.1 $"[11:-2]

from Products.Zuul.interfaces import IThresholdInfo, IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IVGuestInfo(IComponentInfo):
    """
    Info adapter for VGuest components.
    """
    vmName  = schema.Text(title=u"Name", readonly=True,  group='Details')
    vmIp = schema.Text(title=u"Ip Address", readonly=True, group='Details')
    vmOS = schema.Text(title=u"OS Type", readonly=True, group='Details')
    vmState = schema.Text(title=u"Machine State", readonly=True, group='Details')
    cpu_total = schema.Text(title=u"Cores", readonly=True, group='Details')
    mem_total = schema.Text(title=u"Memory [MB]", readonly=True, group='Details')
    vmHDall = schema.Text(title=u"Total HDD Size [GB]", readonly=True, group='Details')
    comapny = schema.Text(title=u"Company", readonly=True, group='Details')
    services = schema.Text(title=u"Service", readonly=True, group='Details')

class IVDatastoreInfo(IComponentInfo):
    """
    Info adapter for VDatastore components.
    """
    #status = schema.Text(title=u"Status", readonly=True, group='Overview')
    vdName  = schema.Text(title=u"Name", readonly=True,  group='Details')
    vdTotal = schema.Text(title=u"Total", readonly=True, group='Details')
    vdUsed = schema.Text(title=u"Used", readonly=True, group='Details')
    vdFree = schema.Text(title=u"Free", readonly=True, group='Details')
    vdFilesystem = schema.Text(title=u"Filesystem", readonly=True, group='Details')
    vdVersion = schema.Text(title=u"Version", readonly=True, group='Details')
    vdPath = schema.Text(title=u"Path", readonly=True, group='Details')

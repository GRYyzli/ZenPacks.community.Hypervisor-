/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');


#var ZEvActions = Zenoss.events.EventPanelToolbarActions;

ZC.VGuestPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'Guest',
            autoExpandColumn : 'vmName',
            sortInfo: {
        	field: 'vmName',
        	direction: 'ASC'
            },
            fields: [
        	{name: 'uid'},
        	{name: 'severity'},
                {name: 'vmName'},
                {name: 'vmIp'},
                {name: 'vmOS'},
                {name: 'vmState'},
            },
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true
	    },{
                id: 'name',
                dataIndex: 'vmName',
                header: _t('VM Name'),
            },{
                id: 'vmIp',
                dataIndex: 'vmIp',
                header: _t('vmIp')
            },{
                id: 'vmOs',
                dataIndex: 'vmOS',
                header: _t('vmOS')
            },{
                id: 'vmState',
                dataIndex: 'vmState',
                header: _t('vmState'),
            }]
        });
        ZC.VGuestPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('VGuestPanel', ZC.VGuestPanel);

ZC.registerName('VGuest', _t('Virtual Machine'), _t('Virtual Machines'));


})();


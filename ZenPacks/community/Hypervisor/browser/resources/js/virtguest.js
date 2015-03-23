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

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.GuestPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'Virtual Guest',
            fields: [
                {name: 'vmName'},
                {name: 'vmIp'},
                {name: 'vmOS'},
                {name: 'vmState'},
                {name: 'cpu_total'},
                {name: 'mem_total'},
                {name: 'vmHDall'},
                {name: 'company'},
                {name: 'service'},
            ],
            columns: [{
//                id: 'severity',
//                dataIndex: 'severity',
//                header: _t('Events'),
//                renderer: Zenoss.render.severity,
//                width: 60
//            },{
                id: 'vmName',
                flex: 1,
                dataIndex: 'vmName',
                header: _t('Name')
            },{
                id: 'vmIp',
                dataIndex: 'vmIp',
                header: _t('Ip Address'),
                sortable: true,
                width: 120
            },{
                id: 'vmOS',
                dataIndex: 'vmOS',
                header: _t('OS Type'),
                sortable: true,
                width: 550
            },{
                id: 'cpu_total',
                dataIndex: 'cpu_total',
                header: _t('Cores'),
                sortable: true,
                width: 100
            },{
                id: 'mem_total',
                dataIndex: 'mem_total',
                header: _t('Memory [MB]'),
                sortable: true,
                width: 100
            },{
                id: 'vmHDall',
                dataIndex: 'vmHDall',
                header: _t('Total HDD Size [GB]'),
                sortable: true,
                width: 100
            },{
                id: 'company',
                dataIndex: 'company',
                header: _t('Company'),
                sortable: true,
                width: 100
            },{
                id: 'service',
                dataIndex: 'service',
                header: _t('Service'),
                sortable: true,
                width: 100
            },{
                id: 'vmState',
                dataIndex: 'vmState',
                header: _t('Machine State'),
                renderer: Zenoss.render.pingStatus,
                sortable: true,
                width: 100
	    }]
        });
        ZC.GuestPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('GuestPanel', ZC.GuestPanel);
ZC.registerName('Guest', _t('Virtual Machine'), _t('Virtual Machines'));


})();


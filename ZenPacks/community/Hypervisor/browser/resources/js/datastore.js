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

ZC.DatastorePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'Virtual Datastore',
            fields: [
                {name: 'vdName'},
                {name: 'vdTotal'},
                {name: 'vdUsed'},
                {name: 'vdFree'},
            ],
            columns: [{
//               id: 'severity',
//               dataIndex: 'severity',
//                header: _t('Events'),
//                renderer: Zenoss.render.severity,
//                width: 60
//            },{
                id: 'vdName',
                dataIndex: 'vdName',
                header: _t('Name'),
                width: 350 
            },{
                id: 'vdTotal',
                dataIndex: 'vdTotal',
                header: _t('Total capacity [GB]'),
            },{
                id: 'vdUsed',
                dataIndex: 'vdUsed',
                header: _t('Used capacity [GB]'),
                width: 150 
            },{
                id: 'vdFree',
                dataIndex: 'vdFree',
                header: _t('Free capacity [GB]'),
                width: 150 
            },{
                id: 'vdFilesystem',
                dataIndex: 'vdFilesystem',
                header: _t('Filesystem'),
                width: 150 
            },{
                id: 'vdVersion',
                dataIndex: 'vdVersion',
                header: _t('Version'),
                width: 150 
            },{
                id: 'vdPath',
                dataIndex: 'vdPath',
                header: _t('Path'),
                width: 200 
            }]
        });
        ZC.DatastorePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('DatastorePanel', ZC.DatastorePanel);
ZC.registerName('Datastore', _t('Datastore'), _t('Datastores'));


})();


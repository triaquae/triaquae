Ext.onReady(function() {
	Ext.QuickTips.init();

	Ext.define('MyService', {
		extend : 'Ext.data.Model',
		fields : [ 'Host', 'Service', 'Status', 'Info' ]
	});

	var oStore = Ext.create('Ext.data.Store', {
		model : 'MyService',
		proxy : {
			type : 'ajax',
			// url: '/status/',
			reader : {
				type : 'json'
			// root: 'services'
			}
		}
	});
	oStore.on('datachanged', function(store, eopts){
		var cri_cnt = 0;
		for(var i = 0; i < store.data.items.length; i++){
			var d = store.data.items[i].raw;
			if (d.Status === 'Critical')
				cri_cnt+=1;
		};
		$('td.ss-summary-Critical').html(cri_cnt);
		$('div.ss-summary-time').html('Last Updated at: '+new Date());
	});

	var myData = [ {
		Host : 'Master',
		Service : 'testa',
		Status : 'ok',
		Info : '4test a'
	}, {
		Host : '192.168.0.1',
		Service : 'testa',
		Status : 'Critical',
		Info : '4test b'
	}, {
		Host : '192.168.0.1',
		Service : 'testb',
		Status : 'ok',
		Info : '4test b'
	}, {
		Host : '192.168.0.1',
		Service : 'testc',
		Status : 'ok',
		Info : '4test b'
	}, {
		Host : '192.168.0.1',
		Service : 'testd',
		Status : 'ok',
		Info : '4test b'
	}, {
		Host : '192.168.0.1',
		Service : 'teste',
		Status : 'ok',
		Info : '4test b'
	}, {
		Host : 'c',
		Service : 'testc',
		Status : 'ok',
		Info : '4test c, server status is ok!'
	} ];

	Ext.create('Ext.grid.GridPanel', {
		columns : [ {
			header : "Host",
			sortable : true,
			dataIndex : 'Host',
		}, {
			header : "Service",
			sortable : true,
			dataIndex : 'Service'
		}, {
			header : "Status",
			sortable : true,
			dataIndex : 'Status'
		}, {
			header : "Info",
			sortable : true,
			dataIndex : 'Info',
			flex : 3
		} ],
		autoHeigth : true,
		enableColumnResize : false,
		enableColumnMove : false,
		store : oStore,
		renderTo : 'grid-status',
		listeners : {
			render : function() {
				this.store.loadRawData(myData);
			}
		}
	});

	setInterval(function() {
		oStore.loadRawData(myData);
	}, 30 * 1000);
});

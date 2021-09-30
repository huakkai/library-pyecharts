odoo.define('load_echarts_bar', function (require) {
    "use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');
    var AbstractAction = require('web.AbstractAction');


    var Bar = AbstractAction.extend({
        template: 'echarts_bar_template',

        init: function(parent, data){
            return this._super.apply(this, arguments);
        },

        start: function(){
            return true;
        },


    });
    core.action_registry.add('load_echarts_bar', Bar);
});
